from django.db import models
from django.contrib.auth import get_user_model
# from django.contrib.auth.models import User

# Create your models here.
user = get_user_model()

class Course(models.Model):
    picture = models.ImageField(
        upload_to='course_picture',
        default='course_picture/default.jpg')
    # video = models.FileField(upload_to='profile_video')
    cost = models.IntegerField()
    title = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(user,on_delete=models.CASCADE)
    likes = models.ManyToManyField(user, related_name="course_likes", blank=True)
    description = models.TextField()
    requirements = models.TextField()
    
    def __str__(self) -> str:
        return f"{self.title}|{self.body[:20]}"
    
class Comment(models.Model):
    body = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(user,on_delete=models.CASCADE)
    approved = models.BooleanField(default=False)
    
    

    def __str__(self) -> str:
        return f"{self.course.title}|{self.body[:40]}"
    
class Event(models.Model):
    picture = models.ImageField(
        upload_to='event_picture',
        default='event_picture/default.jpg')
    title = models.CharField(max_length=350)
    cost = models.IntegerField()
    date = models.DateTimeField()
    time = models.TimeField()
    description = models.TextField()
    location = models.CharField(max_length=200, null=True, blank=True)
    tags = models.TextField()
    parking_instructions = models.TextField()
    likes = models.ManyToManyField(user, related_name="event_likes", blank=True)
    
