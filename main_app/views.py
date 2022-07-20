from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Course,Comment,Event
from .forms import CourseForm,CommentForm,EventForm
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
# Create your views here.

def index(request):
    return render(request, 'main_app/index.html', {})

def index2(request):
    return render(request, 'main_app/index-2.html', {})

@login_required(login_url='/accounts/sign-in/')
def course(request, id):
    c = get_object_or_404(Course, id=id)
    if request.method == 'POST':
        comment = CommentForm(request.POST)
        if comment.is_valid:
            comment_object = comment.save(commit=False)
            comment_object.Course = c
            comment_object.author = request.user
            comment_object.save()
    
    
    f = Comment.objects.filter(course=c).order_by('-date')        
    form = CommentForm()
            
    return render(request, 'main_app/course.html', {'course': c ,'comments': f ,'form': form})
    # return render(request, 'main_app/course.html',{})


# @login_required
def courses(request):
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid:
            form.save()
    courses = course.objects.all().order_by('-date')[:20]
    form = CourseForm()
    return render(request,
                  'main_app/course.html',
                  {"courses": courses,
                   "form": form})

def event(request, id=id):
    e = get_object_or_404(Event, id=id)
    if request.method == 'POST':
        comment = CommentForm(request.POST)
        if comment.is_valid:
            comment_object = comment.save(commit=False)
            comment_object.Event = e
            comment_object.author = request.user
            comment_object.save()
    
    f = Comment.objects.filter(event=e).order_by('-date')        
    form = CommentForm()
            
    return render(request, 'main_app/course.html', {'event': e ,'comments': f ,'form': form})

def events(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid:
            form.save()
    events = Event.objects.all().order_by('-date')[:20]
    form = EventForm()
    return render(request,
                  'main_app/events.html',
                  {"events": events,
                   "form": form})

def search(request):
    # courses = Course.objects.filter(status=1)
    # if request.method == 'GET':
    #     #print(request.GET.get('s'))
    #     # if s := request.GET.get('s'): #use this method only when your using python version 3.8 and above
    #     if request.GET.get('s'):
    #         s =  request.GET.get('s')
    #         courses = courses.filter(content__contains=s)
    
    # context = {'courses':courses}
    return render(request,'main_app/search.html',{})


