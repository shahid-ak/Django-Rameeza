from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from .models import lenders,catagories,books
# Create your views here.

def index(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        return redirect('login')

def home(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            cats=catagories.objects.all()
            return render(request,'adminhome.html',{'catagories':cats})
        else:
            cats=catagories.objects.all()
            new_books = books.objects.all().order_by('-id')[:4]
            return render(request,'home.html',{'catagories':cats,'books':new_books})
    return redirect('login')

def login(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method=='POST':
        usn=request.POST['usn']
        password=request.POST['password']
        user=auth.authenticate(username=usn,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('home')
    return render(request,'login.html')

def register(request):
    if request.user.is_authenticated:
        return redirect('home')
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

def addbook(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            if request.method == 'POST':
                name=request.POST['book']
                discription=request.POST['discription']
                author=request.POST['author']
                catagory=request.POST['catagory']
                img=request.FILES['img']
                submit=books(bookname=name,discription=discription,author=author,catagory=catagory,img=img)
                submit.save()
                cat=catagories.objects.get(name=catagory)
                cat.count+=1
                cat.save()
                return redirect('/home')
    return redirect('/login')

def addcatagory(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            if request.method=='POST':
                catagory=request.POST['catagory']
                submit=catagories(name=catagory)
                submit.save()
                return redirect('/home')
    return redirect('/login')

def delcatagory(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            if request.method=='POST':
                catagory=request.POST['catagory']
                cat=catagories.objects.get(name=catagory)
                if cat.count == 0:
                    catagories.objects.filter(name=catagory).delete()
                    return redirect('/home')
                else:
                    pass
    return redirect('/login')

def allbooks(request):
    if request.user.is_authenticated:
        all_books = books.objects.all()
        cat = catagories.objects.all()
        return render(request,'books.html',{'books':all_books,'catagories':cat})
    return redirect('/login')

def opencatagory(request,cat_id):
    if request.user.is_authenticated:
        cat = catagories.objects.get(id=cat_id)
        all_books = books.objects.filter(catagory=cat.name)
        cat = catagories.objects.all()
        return render(request,'books.html',{'books':all_books,'catagories':cat})
    return redirect('/login')

def viewbook(request,book_id):
    if request.user.is_authenticated:
        book = books.objects.get(id=book_id)
        return render(request,'viewbook.html',{'book':book})
    return redirect('/login')

def delbook(request,book_id):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            books.objects.filter(id=book_id).delete()
            return redirect('/books')
    return redirect('/login')

def users(request):
    if request.user.is_authenticated:
        all_users = lenders.objects.all()
        return render(request,'allusers.html',{'users':all_users})
    return redirect('/login')

def logout(request):
    auth.logout(request)
    return redirect('/login')