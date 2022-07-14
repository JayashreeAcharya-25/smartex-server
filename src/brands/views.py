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
        

# class UpdateBrands(APIView):
#     def put(self, request):
#         try:
#             data = request.data
#             brand = Brands.objects.get(id = data['id'])
           
#         except:
#             return Response(status=status.HTTP_404_NOT_FOUND)

#         serializer = BrandSerializer(instance=brand, data=request.data)
#         if serializer.is_valid():
            
#             serializer.save()
#             print(serializer.data)
#             response = Response(serializer.data)
#             response.data = {
#                 'message': 'Updated Successfully!',
#                 'data': serializer.data,
#                 'status': status.HTTP_200_OK
#             }
#             return response
#         else:
#             return Response(serializer.errors)


class UpdateBrands(APIView):
    def put(self, request):

        try:
            data = request.data
            print("request_data", data)
            brand_id = data['id']
            brand_slno = data['brand_slno']
            brand_name = data['brand_name']
            brand_image = data['brand_image']

            # brand = Brands.objects.get(id = brand_id)

            # print('brands', brand)

            update_data = Brands.objects.get(id = brand_id).bulk_update(
                brand_slno = brand_slno,
                brand_name = brand_name,
                brand_image = brand_image
            )
            print("updated", update_data)

            response = Response(update_data)
            response.data = {
                'message': 'Updated Successfully!',
                
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