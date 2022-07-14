from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import Category
from . serializer import CategorySerializer
# Create your views here.

class AddCategory(APIView):
    def post(self, request):
        try:
            serializer = CategorySerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            response = Response(serializer.data)
            response.data = {
                'message': 'Category Created Successfully!',
                'data': serializer.data,
                'status': status.HTTP_200_OK
            }
            return response

        except Exception as e:    
            return Response(format(e))
        

class GetCategory(APIView):
    def get(self, request):
        try:
            category = Category.objects.all()
            serializer = CategorySerializer(category, many=True)
            response = Response()
            response.data = {
                'data': serializer.data,
                'status': status.HTTP_200_OK
            }
            return response

        except Exception as e:    
            return Response(format(e)) 


class UpdateCategory(APIView):
    def put(self, request):
        try:
            data = request.data
            category = Category.objects.get(id = data['id'])
        
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = CategorySerializer(instance=category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            response = Response(serializer.data)
            response.data = {
                'message': 'Updated Successfully!',
                'data': serializer.data,
                'status': status.HTTP_200_OK
            }
            return response
        else:
            return Response(serializer.errors)


class DeleteCategory(APIView):
    def delete(self, request, id=0):
        try:
            category = Category.objects.filter(id = id)
            category.delete()
            response = Response(category)
            response.data = {
                'data': category,
                'message': 'Deleted Successfully',
                'status': status.HTTP_200_OK
            }

        except Exception as e:
            return Response(format(e))