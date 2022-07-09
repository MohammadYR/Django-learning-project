from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'main_app/index.html', {})

def index2(request):
    return render(request, 'main_app/index-2.html', {})

def course(request):
    return render(request, 'main_app/course.html', {})

def event(request):
    return render(request, 'main_app/event.html', {})

def events(request):
    return render(request, 'main_app/events.html', {})

def search(request):
    return render(request, 'main_app/search.html', {})

def signin(request):
    return render(request, 'main_app/sign-in.html', {})

def signup(request):
    return render(request, 'main_app/sign-up.html',{})
