from email import message
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from django.core.mail import EmailMessage


import authendicate

# Create your views here.


@csrf_protect
def signup(request):

    if request.method == "POST":
       username=request.POST["username"]
       password=request.POST["password"]
       password1=request.POST["password2"]
       email=request.POST["email"]
       
       if password==password1:
            if User.objects.filter(username=username).exists():
                    messages.error(request,"user name already exist")
                    return redirect('signup') 
            elif User.objects.filter(email=email).exists():
                messages.error(request,"mail already taken")
                return redirect('signup')
            else:    
                user=User.objects.create_user(username=username,password=password,email=email)
                user.is_active=False
                email_subject='Activation mail from expense application'
                email_body='Hi There'
                email=EmailMessage(
                    'email_subject',
                    'email_body',
                    'heman2097@gmail.com',
                    [email]
                )
                email.send(fail_silently=True)
                return redirect("loginpage")
       else:
           messages.error(request,"password not matching")
           return redirect('signup')

    return render(request,'base/authendicates/signup.html',)

def loginpage(request):
    if request.method == "POST":
        username=request.POST.get("username")
        password=request.POST.get("password")

        try:
          user =User.objects.get(username=username)
        except:
            messages.error(request,'user doesnt exits')
            return redirect('loginpage')   

        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'incorrect password')
            return redirect('loginpage')  
    else:
        return render(request,'base/authendicates/loginpage.html')  

def logoutpage(request):
    logout(request)
    return redirect('loginpage')






