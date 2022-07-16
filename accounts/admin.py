from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    pass

@admin.register(models.SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    pass 