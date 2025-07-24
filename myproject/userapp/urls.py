from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name='index'),
    path('signup', views.signup, name='signuppg'),
    path('signin',views.signin,name='signinpg'),
    path('profile',views.profile,name='profilepg'),
    path('loadsignup',views.signupuser,name='signupuser'),
    path('loadsignin',views.signinuser,name='signinuser'),
    path('loadlogout',views.userlogout,name='logout'),
]