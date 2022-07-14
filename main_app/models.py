from django.db import models
from django.contrib.auth import get_user_model
# from django.contrib.auth.models import User

# Create your models here.
user = get_user_model()

class Course(models.Model):
    picture = models.ImageField(
        upload_to='profile_picture',
        default='profile_picture/default.jpg')
    title = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(user,on_delete=models.CASCADE)
    likes = models.ManyToManyField(user, related_name="Course_likes", blank=True)
    
    
    def __str__(self) -> str:
        return f"{self.title}|{self.body[:20]}"
    
class Comment(models.Model):
    body = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(user,on_delete=models.CASCADE)
    

    def __str__(self) -> str:
        return f"{self.course.title}|{self.body[:40]}"