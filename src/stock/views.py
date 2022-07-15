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
            print(data)
            stock = Stock.objects.get(id = data['id'])
        
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = StockSerializer(instance=stock, data=request.data)
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