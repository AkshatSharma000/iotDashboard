from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home , name="home"),
    path('signup/',views.signup, name="signup"),
    path('signin/',views.signin, name="signin"),
    path('signout/',views.signout, name="signout"),
    path('Index/', views.Index, name="Index"),
]
