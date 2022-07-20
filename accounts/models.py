from django.db import models
from django.forms import Widget
from django.urls import reverse
from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.contrib.auth.models import User

from .managers import CustomUserManager

# Create your models here.
class User(AbstractUser):
    # user = models.OneToOneField(User,on_delete=models.CASCADE)
    username = None
    email = models.EmailField('email address', unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    age = models.IntegerField(null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    education = models.TextField(null=True, blank=True)
    objects = CustomUserManager()
    
     # def __str__(self):
    #     return self.email

    # def get_absolute_url(self):
    #     return reverse("profile", kwargs={"fullname": self.fullname})
    
class SocialMedia(models.Model):
    TYPES = (
        ('f', 'facebook'),
        ('l', 'linked in'),
    )
    url = models.URLField()
    type = models.CharField(max_length=1, choices=TYPES)
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name="social_media_set")
