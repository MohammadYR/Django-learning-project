from django.contrib import admin
from .models import Course,Comment,Event
# Register your models here.


# @admin.register(models.Course)
# class CourseAdmin(admin.ModelAdmin):
#     pass


admin.site.register(Course)
admin.site.register(Event)
admin.site.register(Comment)
