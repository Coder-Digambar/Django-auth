from django.urls import path
from .import views

urlpatterns = [
    path('',views.indexpage,name='indexpg'),
    path('login',views.loginpage,name='loginpg'),
    path('register',views.registerpage,name='registerpg'),
    path('profile',views.profilepage,name='profilepg'),
    path('userregister', views.userregister, name='uregister'),
    path('userlogin', views.userlogin, name='ulogin'),
    path('userlogout', views.userlogout, name='logout'),
]