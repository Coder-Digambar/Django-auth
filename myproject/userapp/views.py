from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages,auth
# Create your views here.
def index(request):
    return render(request,'index.html')

def signup(request):
    return render(request,'signup.html')

def signin(request):
    return render(request,'signin.html')

def profile(request):
    #get session
    if 'sname' in request.session:  #checking session is set or not
        uname = request.session.get('sname')
        return render(request,'profile.html',{'name':uname})
    else:

        return render(request,'signin.html')

def signupuser(request):
    if request.method == 'POST':
        ufname = request.POST.get('fname')
        ulname = request.POST.get('lname')
        uuname = request.POST.get('uname')
        umail = request.POST.get('gmail')
        upass = request.POST.get('pass')
        ucpass = request.POST.get('fpass')

        if(upass==ucpass):
            if(user.objects.filter(username=uuname)):
                messages.success(request,'Username Already Exist !!')
                return redirect('signuppg')
            elif(user.objects.filter(email=umail)):
                messages.success(request,'Mail Already Exist !!')
                return redirect('signuppg')
            else:
                obj = user()
                obj.firstname = ufname
                obj.lastname = ulname
                obj.email = umail
                obj.username = uuname
                obj.upass = upass
                obj.save()
                messages.success(request,'User Created !!')
                return redirect('signuppg')
        else:
            messages.success(request,'Password Not Match !!!')
            return redirect('signuppg')
    else:
        return render(request,'signup.html')

def signinuser(request):
    if request.method == 'POST':
        uuname = request.POST.get('uname')
        upass = request.POST.get('pass')

        myuser = user.objects.filter(username=uuname,upass=upass).count()

        if(myuser==1):
            #set session
            request.session['sname'] = uuname
            return redirect('profilepg')
        else:
            messages.success(request,'Invalid Username & Password !')
            return redirect('signinpg')

def userlogout(request):
    #delete session
    request.session.flush()
    return redirect('signinpg')