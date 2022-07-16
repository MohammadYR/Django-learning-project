from django import forms
from .models import Course,Comment

# class EmailForm(forms.Form):
#     pass

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['picture','title','body']
        
        
class CommentForm(forms.ModelForm):
     class Meta:
          model=Comment
          fields = ['body']
          widgets = {
            'body': forms.Textarea(attrs={'cols': 10, 'rows': 10,'class':"comment-body"}),
        }
        
    
    
    
    # title = forms.CharField(max_length=20)
    # body = forms.CharField(max_length=300)
    # author = forms.CharField(max_length=20)
    # email = forms.EmailField()