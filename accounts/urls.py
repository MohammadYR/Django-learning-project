from django.urls import path
from . import views



urlpatterns = [
    path('sign-in/',views.signin ,name='sign-in'),
    path('sign-up/',views.signup ,name='sign-up'),

]