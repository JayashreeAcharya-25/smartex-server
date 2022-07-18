from urllib import response
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import Product
from . serializer import ProductSerializer

# Create your views here.
class AddProduct(APIView):
    def post(self, request):
        try:
            serializer = ProductSerializer(data=request.data)

            serializer.is_valid(raise_exception=True)
            serializer.save()
            
            response = Response(serializer.data)
            response.data = {
                'message': 'Product Created Successfully!',
                'data': serializer.data,
                'status': status.HTTP_200_OK
            }
            return response

        except Exception as e:    
            return Response(format(e))
        

class GetProduct(APIView):
    def get(self, request):
        try:
            category = Product.objects.all()

            serializer = ProductSerializer(category, many=True)

            response = Response()
            response.data = {
                'data': serializer.data,
                'status': status.HTTP_200_OK
            }
            return response

        except Exception as e:    
            return Response(format(e)) 



class UpdateProduct(APIView):
    def patch(self, request):
        try:
            data = request.data
            id = data['id']

            product = Product.objects.get(id = id)

            serializer = ProductSerializer(product, data=request.data, partial=True)
            
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



class DeleteProduct(APIView):
    def delete(self, request, id=0):
        try:
            
            product = Product.objects.filter(id = id)

            product.delete()

            response = Response(product)
            response.data = {
                'data': product,
                'message': 'Deleted Successfully',
                'status': status.HTTP_200_OK
            }
            return response

        except Exception as e:
            return Response(format(e))