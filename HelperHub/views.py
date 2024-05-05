from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,'index.html')

def login_user(request):
    if request.method=="POST":
        usern = request.POST.get("username")
        passw = request.POST.get("password")
        user = authenticate(request, username=usern, password=passw)
        try:
            login(request,user)
            return render(request,"indexnew.html")
        except:
            messages.error(request,"Email or Password incorrect")
            return render(request,"indexnew.html")
    return render(request,'login.html')

@login_required
def logout_user(request):
    logout(request)
    return render(request,"index.html")

def register(request):
    if request.user.is_authenticated:
        return render(request,"indexnew.html")

    if request.method == "POST":
        fname = request.POST.get("firstname")
        lname = request.POST.get("lastname")
        mail = request.POST.get("email_address")
        pasworrd = request.POST.get("password")
        print(fname,lname,mail)
        try:    
            user = User.objects.create_user(username=mail,
                                                    email=mail,
                                                    password=pasworrd
                                                    )
            user.last_name=lname
            user.first_name=fname
            user.save()
            login(request,user)
            return render(request,"indexnew.html")
        except Exception as e:
            print(e)
            messages.error(request,"Email already registered")
            return render(request,"individual-registration.html")
    return render(request,'individual-registration.html')

def getInTouch(request):
    return render(request,'get-in-touch.html')

def about(request):
    return render(request,'about.html')


