from django.shortcuts import render,redirect
from .models import *
# Create your views here.

def bookform(request):
    return render(request,'bookform.html')

def insertbook(request):
    if request.method == 'POST':

        name = request.POST.get('bname')
        author = request.POST.get('bauthor')
        doc = request.FILES['bdoc']
        cover = request.FILES['bcover']

        obj = Book()
        obj.name = name
        obj.author = author
        obj.docs = doc

        obj.cover = cover

        obj.save()
        return redirect('bkform')
    else:
        return render(request,'bookform.html')

def showbook(request):
    obj = Book.objects.all()
    return render(request,'showbook.html',{'book':obj})