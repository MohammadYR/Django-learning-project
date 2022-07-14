from django import forms
from .models import Course

class EmailForm(forms.Form):
    pass

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['picture','title','body']
        
    
    
    
    # title = forms.CharField(max_length=20)
    # body = forms.CharField(max_length=300)
    # author = forms.CharField(max_length=20)
    # email = forms.EmailField()