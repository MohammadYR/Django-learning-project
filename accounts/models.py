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
    fullname = models.CharField(max_length=70)
    email = models.EmailField()
    objects = CustomUserManager()
    

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
