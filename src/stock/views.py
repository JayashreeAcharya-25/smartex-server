from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import Stock
from . serializer import StockSerializer
# Create your views here.

class AddStock(APIView):
    def post(self, request):
        try:
            serializer = StockSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            response = Response(serializer.data)
            response.data = {
                'message': 'Stock Created Successfully!',
                'data': serializer.data,
                'status': status.HTTP_200_OK
            }
            return response

        except Exception as e:    
            return Response(format(e))
        

class GetStock(APIView):
    def get(self, request):
        try:
            stock = Stock.objects.all()
            serializer = StockSerializer(stock, many=True)
            response = Response()
            response.data = {
                'data': serializer.data,
                'status': status.HTTP_200_OK
            }
            return response

        except Exception as e:    
            return Response(format(e)) 


class UpdateStock(APIView):
    def put(self, request):
        try:
            data = request.data
            id = data['id']
            
            stock = Stock.objects.get(id = id)

            serializer = StockSerializer(stock, data=request.data, partial=True)
            
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


class DeleteStock(APIView):
    def delete(self, request, id=0):
        try:
            stock = Stock.objects.filter(id = id)
            stock.delete()
            response = Response(stock)
            response.data = {
                'data': stock,
                'message': 'Deleted Successfully',
                'status': status.HTTP_200_OK
            }
            return response

        except Exception as e:
            return Response(format(e))