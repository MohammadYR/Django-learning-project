from email import message
from django.shortcuts import get_object_or_404, render,redirect
from django.http import Http404, HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.utils.http import urlencode
from django.contrib import messages

from accounts.models import User
from .forms import UserForm

def signin(request):
    if request.method == "POST":
        fullname = request.POST.get("fullname")
        password = request.POST.get("password")
        email = request.POST.get("email")
        user = authenticate(email=email, password=password)

        if user:
            login(request,user)
            return redirect(to=reverse('index'))
        else:
            messages.add_message(request,messages.ERROR,"email or password is wrong!")

    return render(request,'accounts/sign-in.html',{})

def signout(request):
    logout(request)
    return redirect(to=reverse('index'))


def signup(request):
    if request.method == "POST":
        form=UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,"Your account has been created successfully! you can now login")
            return redirect(to=reverse('signin'))
        else:
            return render(request,'accounts/sign-up.html',{'form':form})

    elif request.method == "GET":
        form = UserForm()
        return render(request,'accounts/sign-up.html',{'form':form})
    else:
        return HttpResponse("404")

    

