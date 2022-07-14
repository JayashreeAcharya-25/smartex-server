from django.urls import path
from . views import AddBrands, GetBrands, UpdateBrands, DeleteBrands

urlpatterns=[
    path('addbrand', AddBrands.as_view()),
    path('getbrand', GetBrands.as_view()),
    path('updatebrand', UpdateBrands.as_view()),
    path('deletebrand/<int:id>', DeleteBrands.as_view()),
]