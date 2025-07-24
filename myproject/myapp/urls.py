from django.urls import path
from .import views
urlpatterns=[
    path('',views.hm,name='home'),
    path('about',views.ab,name='about'),
    path('formpage',views.fm,name='form'),
    path('insertdata',views.insertdata,name='insert'),
    path('showdata',views.showdata,name='show'),
    #Passing Param As Url
    path('edit/<int:id>',views.getdata,name='edit'),
    path('update/<int:id>',views.updatedata,name='update'),
    path('delete/<int:id>',views.deletedata,name='delete'),


    path('status/<int:id>/<str:st>',views.stdstatus,name='status'),
]
