import datetime
from jwt import PyJWT
from rest_framework.exceptions import AuthenticationFailed
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import User
from . serializer import UserSerializer

# Create your views here.

class SignUp(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request):
        try:
            serializer = UserSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            response = Response(serializer.data)
            response.data = {
                'message': 'User Created Successfully!',
                'data': serializer.data,
                'status': status.HTTP_200_OK
            }
            return response

        except Exception as e:    
            return Response(format(e))


class Login(APIView):
    def post(self, request):
        try:
            email = request.data['email']
            password = request.data['password']

            user = User.objects.filter(email = email).first()

            if user is None:
                raise AuthenticationFailed("User Not Found")
            
            if not user.check_password(password):
                raise AuthenticationFailed('Incorrect password')

            # for jwt token first we need to create payload
            payload ={
                'id': user.id,
                'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60), # expires after 1hr.
                'iat': datetime.datetime.utcnow()  # iat is the date, were token is created.
            }

            token = PyJWT.encode(payload, 'secret', algorithm='HS256').decode('utf-8')  #1st params : payload, 2nd params : SECRET_KEY, 3rd params : algo

            response = Response()

            # set the token to cookies
            response.set_cookie(key='jwt', value=token, httponly=True)

            data = {
                'id': user.id,
                'username': user.username,
                'email': user.email
            }

            response.data = {
                'message': "Logged In",
                'jwt': token,
                'data': data,
            }

            return response
        
        except Exception as e:
            print(format(e))


class UserView(APIView):

    def get(self, request):
        
        token = request.COOKIES.get('jwt')

        if not token:
            # return Response('Error')
            raise AuthenticationFailed('Unauthenticated')
        
        try:
            payload = PyJWT.decode(token, 'secret', algorithm=['HS256'])
        except PyJWT.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated')

        user = User.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(user)

        response = Response(serializer.data)
        response.data = {
                'jwt': token,
                'data': serializer.data,
            }
        return response

class Logout(APIView):

    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data ={
            'message': 'Success'
        }
        return response