from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.
def indexpage(request):
    return render(request,'index.html')

def loginpage(request):
    return render(request,'login.html')

def registerpage(request):
    return render(request,'register.html')

def profilepage(request):
    return render(request,'profile.html')

def userregister(request):
    if request.method == 'POST':
        ufname = request.POST.get('fname')
        ulname = request.POST.get('lname')
        uuname = request.POST.get('uname')
        umail = request.POST.get('gmail')
        upass = request.POST.get('pass')
        ucpass = request.POST.get('fpass')



#Checking Pass with Confirm
        if (upass==ucpass):
            obj = User.objects.create_user(first_name=ufname,last_name=ulname,username=uuname,email=umail,password=upass)
            obj.save()
            messages.success(request,'User Registerd !!! Please Login !')
            return redirect('/register')
        else:
            messages.success(request, 'Password Not Match !!!')
            return redirect('/register')
    else:
        return render(request,'register.html')

def userlogin(request):
    if request.method == 'POST':
        uuname = request.POST.get('uname')
        upass = request.POST.get('pass')

        myuser = auth.authenticate(username=uuname,password=upass)
        if myuser is not None:      #its should be unique pair
            auth.login(request,myuser)
            return redirect('profilepg')
        else:
            messages.success(request,'UserName or Password Incorrect !!!')
            return redirect('loginpg')
    else:
        return render(request,'login.html')


def userlogout(request):
    auth.logout(request)
    return redirect('loginpg')