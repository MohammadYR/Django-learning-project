from django import forms
from .models import Course,Comment,Event
from django.forms import Widget

# class EmailForm(forms.Form):
#     pass

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'
        
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
        widgets = {
            'body': forms.Textarea(attrs={'cols': 10, 'rows': 10,'class':"comment-body"}),
        }
        
    
class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'   
    
    