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
    def patch(self, request):
        
        try:
            data = request.data
            id = data['id']

            category = Category.objects.get(id = id)
            serializer = CategorySerializer(category, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                
                response = Response()
                response.data = {
                    'message': 'Updated Successfully!',
                    'data': serializer.data,
                    'status': status.HTTP_200_OK
                }
                return response
                
        except Exception as e:
            return Response(format(e))


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
            return response

        except Exception as e:
            return Response(format(e))