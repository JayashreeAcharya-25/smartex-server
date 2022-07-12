from django.urls import path
from . views import AddProduct, GetProduct, UpdateProduct, DeleteProduct

urlpatterns=[
    path('addproduct', AddProduct.as_view()),
    path('getproduct', GetProduct.as_view()),
    path('updateproduct', UpdateProduct.as_view()),
    path('deleteproduct/<int:id>', DeleteProduct.as_view()),
]