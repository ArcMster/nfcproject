from django.shortcuts import render, redirect
from .models import Stories, Videos
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages


# Create your views here.
global count
count = 0

def home(request):
    return render(request,'home.html')


def videos(request):
    videos = Videos.objects.all()

    return render(request,'video.html',{'videos':videos})

def stories(request):
    stories = Stories.objects.all()
    n=3
    return render(request,'stories.html',{'stories':stories,'n':n})

def add_story(request): 
    name = request.POST['name']
    story = request.POST['story']

    new_story = Stories()
    new_story.name = name
    new_story.story = story
    new_story.save()
    return render(request,'home.html')


def login(request):
    return render(request,'login.html')


def authenticate(request):
    userid = request.POST['userid']
    password = request.POST['password']
    print(userid)
    user = auth.authenticate(username = userid, password=password)
    if user is not None:
        auth.login(request,user)
    else:
        messages.info(request,'Invalid credentials')
        return redirect('login')
    return render(request,'home.html')

def signup(request):
    '''fname = request.POST['fname']
    lname = request.POST['lname']
    email = request.POST['email']'''
    return render(request,'signup.html')


def register(request):
    fname = request.POST['fname']
    lname = request.POST['lname']
    email = request.POST['email']
    uname = request.POST['uname']
    password1 = request.POST['password1']
    password2 = request.POST['password2']

    if password1==password2:
        if User.objects.filter(username=uname).exists():
            messages.info(request,'Username exists')
            return redirect('signup')
        elif User.objects.filter(email=email).exists():
            messages.info(request,'Email already exists')
            return redirect('signup')
        else:
            user = User.objects.create_user(username=uname,password = password1,email = email, first_name = fname, last_name = lname)
            user.save()
            return redirect('login')
    else:
        messages.info(request,'Passwords not matching..!')
        return redirect('signup')



    return HttpResponse(fname)

#Created for test purpose
def next_page(request,n):
    global count
    count += 1
    return HttpResponse(n)


def logout(request):
    auth.logout(request)
    return render(request,'home.html')
