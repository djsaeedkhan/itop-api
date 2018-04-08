from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login
from itop import ItopApi

def Index(request):
    if Session(request) == False: return HttpResponseRedirect('/Login/') 

    return render(request,'index.html',{})

def Dashboard(request):
    if Session(request) == False: return HttpResponseRedirect('/Login/') 
        
    loger= ItopApi.Dashboard()
    status=loger.UserLocal(request)
    return render(request,'dashboard.html',{"status":status})

def Login(request):
    status=""
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        loger= ItopApi.Dashboard()
        status=loger.Login(username,password)
        if status == True:
            request.session['username'] = username
            request.session['password'] = password
            return HttpResponseRedirect('/Dashboard/')
        else:
            status="Failed Login"
    return render(request,'login.html',{"status":status})

def Logout(request):
    del request.session['username']
    del request.session['password']
    return HttpResponseRedirect('/Login/')

def Session(request):
    if request.session.get('username', 0) == 0:
        return False
    else: 
        return True    