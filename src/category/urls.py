from django.urls import path
from . views import AddCategory, GetCategory, UpdateCategory, DeleteCategory

urlpatterns=[
    path('addcategory', AddCategory.as_view()),
    path('getcategory', GetCategory.as_view()),
    path('updatecategory', UpdateCategory.as_view()),
    path('deletecategory/<int:id>', DeleteCategory.as_view()),
]