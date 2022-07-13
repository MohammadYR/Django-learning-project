from django.shortcuts import render

# Create your views here.


def signin(request):
    return render(request, 'accounts/sign-in.html', {})

def signup(request):
    return render(request, 'accounts/sign-up.html',{})
