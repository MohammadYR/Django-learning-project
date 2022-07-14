from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth.decorators import login_required
# Create your views here.


def signin(request):
    # if not request.user.is_authenticated:
    #     if request.method == 'POST':
    #         form = AuthenticationForm(request=request,data=request.POST)
    #         if form.is_valid():
    #             email = form.cleaned_data.get('email')
    #             password = form.cleaned_data.get('password')
    #             user = authenticate(request, email=email , password=password)
    #             if user is not None:
    #                 login(request,user)
    #                 return redirect('/')

    #     form = AuthenticationForm()
    #     context = {'form':form}
        return render(request,'accounts/sign-in.html',{})
    # else:
    #     return redirect('/')

# @login_required
# def signout(request):
#     logout(request)
#     return redirect('/')


def signup(request):
    # if not request.user.is_authenticated:
    #     if request.method == 'POST':
    #         form = UserCreationForm(request.POST)
    #         if form.is_valid():
    #             form.save()
    #             return redirect('/')
    #     form = UserCreationForm()
    #     context = {'form':form}
        return render(request,'accounts/sign-up.html',{})
    # else:
    #     return redirect('/')