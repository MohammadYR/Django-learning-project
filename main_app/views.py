from django.shortcuts import render
from .models import Course
from .forms import CourseForm
# Create your views here.

def index(request):
    return render(request, 'main_app/index.html', {})

def index2(request):
    return render(request, 'main_app/index-2.html', {})

def course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
    
    courses = Course.objects.all()
    form = CourseForm()        
    return render(request, 'main_app/course.html', {'courses': courses ,'form': form})
    # return render(request, 'main_app/course.html',{})


def event(request):
    return render(request, 'main_app/event.html', {})

def events(request):
    return render(request, 'main_app/events.html', {})

def search(request):
    return render(request, 'main_app/search.html', {})

