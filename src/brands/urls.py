from django.urls import path
from . views import AddBrands, GetBrands

urlpatterns=[
    path('addbrand', AddBrands.as_view()),
    path('getbrand', GetBrands.as_view())
]