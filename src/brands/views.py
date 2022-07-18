from functools import partial
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from . serializer import BrandSerializer
from . models import Brands


# Create your views here.

class AddBrands(APIView):

    def post(self, request):
        
        try:
            serializer = BrandSerializer(data=request.data)
            print(request.data)
            
            if serializer.is_valid():
            
                serializer.save()
            
                response = Response(serializer.data)
                response.data = {
                    'data': serializer.data,
                    'message': 'Brand Created Successfully!',
                    'status': status.HTTP_200_OK
                }
                return response
            else:
                return Response({"status": "error", "data": serializer.errors}, status = status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response(format(e))

class GetBrands(APIView):

    def get(self, request):
        try:
            brands = Brands.objects.all()

            serializer = BrandSerializer(brands, many=True)

            response = Response()
            response.data = {
                'data': serializer.data,
                'status': status.HTTP_200_OK
            }
            return response

        except Exception as e:    
            return Response(format(e)) 
        

class UpdateBrands(APIView):
    def patch(self, request):

        try:
            data = request.data
            id = data['id']

            brands = Brands.objects.get(id = id)

            serializer = BrandSerializer(brands, data=request.data, partial=True)
            
            if serializer.is_valid():
                serializer.save()
                response = Response()
                response.data ={
                    'data': serializer.data,
                    'message': 'Update Successfully',
                    'status': status.HTTP_200_OK
                }
                return response

        except Exception as e:    
            return Response(format(e))
        

class DeleteBrands(APIView):
    def delete(self, request, id=0):
        try:
            brand = Brands.objects.filter(id = id)

            brand.delete()

            response = Response(brand)
            response.data = {
                'data': brand,
                'message': 'Deleted Successfully',
                'status': status.HTTP_200_OK
            }
            return response

        except Exception as e:
            return Response(format(e))