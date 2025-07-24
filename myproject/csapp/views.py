from django.shortcuts import render

# Create your views here.
def setcookie(request):
    responce = render(request,'set.html')
    responce.set_cookie('ckname','ram')
    return responce
def getcookies(request):
    uname = request.COOKIES.get('ckname')
    return render(request,'get.html',{'name':uname})

def delcookies(request):
    responce = render(request,'del.html')
    responce.delete_cookie('ckname')
    return responce


def setsession(request):
                    #key        #value
    request.session['user'] = 'digambar'
    return render(request,'setsession.html')

def getsession(request):
    user = request.session.get('user')
    return render(request,'getsession.html',{'name':user})

def delsession(request):
    request.session.flush()
    return render(request,'delsession.html')