from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from .models import lenders
# Create your views here.

def index(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        return redirect('login')

def home(request):
    if request.user.is_authenticated:
        return render(request,'home.html')
    return redirect('login')

def login(request):
    if request.method=='POST':
        usn=request.POST['usn']
        password=request.POST['password']
        user=auth.authenticate(username=usn,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('home')
    return render(request,'login.html')

def register(request):
    if request.method=='POST':
        name=request.POST['name']
        usn=request.POST['usn']
        branch=request.POST['branch']
        password=request.POST['password']
        if User.objects.filter(username=usn).exists():
            messages.info(request,'USN Taken')
            return redirect('/login')
        user = User.objects.create_user(username=usn, password=password, first_name=name)
        user.save()
        usr=lenders(name=name, usn=usn, branch=branch, authid=user.id)
        usr.save()
        user = auth.authenticate(username=usn,password=password)
        auth.login(request,user)
        return redirect('/home')
    return render(request,'register.html')