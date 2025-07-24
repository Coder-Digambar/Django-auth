from django.shortcuts import *
from .models import *

# Create your views here.
def hm(request):
    return render (request,'home.html')
def ab(request):
    return render (request,'about.html')
def fm(request):
    return render(request,'form.html')

def insertdata(request):
    if request.method == 'POST':
        studname = request.POST.get('sname')
        gen = request.POST.get('gender')
        obj =stud()
        obj.name=studname
        obj.gender = gen
        obj.save()
        return redirect('home')
    else:
        return render(request,'form.html')

def showdata(request):
    obj = stud.objects.all()
    return render(request,'showdata.html',{'data':obj})

def getdata(request,id):
    obj = stud.objects.get(id=id)
    return render(request,'editform.html',{'table':obj})

def updatedata(request,id):
    obj = stud.objects.get(id=id)
    uname = request.POST.get('ename')
    gen = request.POST.get('gender')
    obj.name = uname
    obj.gender = gen
    obj.save()
    return redirect('show')
def deletedata(request,id):
    obj = stud.objects.get(id=id)
    obj.delete()
    return redirect('show')

def stdstatus(request,id,st):
    if st=='BLOCK':
        obj = stud.objects.get(id=id)
        obj.status = 'UNBLOCK'
        obj.save()
        return redirect('show')
    else:
        obj = stud.objects.get(id=id)
        obj.status = 'BLOCK'
        obj.save()
        return redirect('show')
