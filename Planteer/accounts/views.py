from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate ,login, logout

from django.contrib import messages
# Create your views here.

def signup_view(request: HttpRequest) :
    if request.method == "POST" :
        try :
            username = request.POST.get("username")
            first_name = request.POST.get("first_name")
            last_name = request.POST.get("last_name")
            email = request.POST.get("email")
            password = request.POST.get("password")
            new_user = User.objects.create_user(username=username,first_name=first_name, last_name=last_name, email=email, password=password)
            new_user.save()
            messages.success(request,"Registered User Successfuly","alert-success")
        
            return redirect('accounts:signin_view')

        except Exception as e :
            print(e)
        
    return render(request, "accounts/signup.html")

def signin_view(request: HttpRequest) :
    if request.method == "POST" :
        try :
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(request, username=username, password=password)
            if user :
                login(request, user)
                messages.success(request,"Logged In Successfuly","alert-success")
                return redirect(request.GET.get('next', '/'))
            else :
                messages.error(request,"Please try again , You credentials are wrong","alert-danger")
        
        except Exception as e :
            print(e)

    return render(request, "accounts/signin.html")

def logout_view(request: HttpRequest) :
    logout(request)
    messages.success(request,"Logged Out Successfuly","alert-success")
    return redirect(request.GET.get('next', '/'))