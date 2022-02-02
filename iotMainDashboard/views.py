from django.http import HttpResponseBadRequest
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import redirect,render
from django.contrib.auth import authenticate,login,logout
from .services import api_info
from .models import device_info
# Create your views here.
def home(request):
    return render(request,"Game/Typing.html")

def Index(request):
    if request.user.is_authenticated:
        device_info(
            details = api_info()
        ).save()
        return render(request,"Game/Index.html",{'data':api_info()})
    else:
        return render(request,"Game/404.html")

def signup(request):
    if request.method =="POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        myuser = User.objects.create_user(username,email,password)
        myuser.first_name = fname
        myuser.last_name = lname
        # myuser.user_name = username

        myuser.save()
        messages.success(request,"Your Account has been successfully created.")

        return redirect('signin')

    return render(request,"Game/signup.html",)

def signin(request):

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request,user)
            fname = user.first_name
            return redirect('Index')
            # return render(request,"Game/Index.html",{'fname': fname})
        else:
            messages.error(request, "Bad Credentials")
            return redirect('home')

    return render(request,"Game/signin.html")

def signout(request):
    logout(request)
    messages.success(request,"Logged Out Successfully!")
    return redirect('home')