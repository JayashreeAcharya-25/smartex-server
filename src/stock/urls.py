from django.urls import path
from . views import AddStock, GetStock, UpdateStock, DeleteStock

urlpatterns=[
    path('addstock', AddStock.as_view()),
    path('getstock', GetStock.as_view()),
    path('updatestock', UpdateStock.as_view()),
    path('deletestock/<int:id>', DeleteStock.as_view()),
]