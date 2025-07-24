from django.urls import path
from .import views
urlpatterns = [
    path('',views.setcookie),
    path('get',views.getcookies,name='getck'),
    path('del',views.delcookies,name='delck'),
    path('sets',views.setsession,name='setsn'),
    path('gets',views.getsession,name='getsn'),
    path('dels',views.delsession,name='delsn'),
]