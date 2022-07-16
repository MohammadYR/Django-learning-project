from django import forms
from django.contrib.auth.forms import UserCreationForm
from . import models
import email

class UserForm(UserCreationForm):
    class Meta:
        model=models.User
        fields='__all__'
 