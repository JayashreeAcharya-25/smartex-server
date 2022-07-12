from django.urls import path
from . views import AddCategory, GetCategory

urlpatterns=[
    path('addcategory', AddCategory.as_view()),
    path('getcategory', GetCategory.as_view())
]