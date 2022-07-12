from django.urls import path
from src.user.views import Logout, SignUp, Login, UserView

urlpatterns=[
    path('register', SignUp.as_view()),
    path('login', Login.as_view()),
    path('getuser', UserView.as_view()),
    path('logout', Logout.as_view()),
]