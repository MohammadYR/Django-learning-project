from django.urls import path
from . import views



urlpatterns = [
    path('index2/',views.index2 ,name='index2'),
    path('course/',views.course,name='course'),
    path('event/',views.event ,name='event'),
    path('events/',views.events ,name='events'),
    path('search/',views.search ,name='search'),
    path('sign-in/',views.signin ,name='sign-in'),
    path('sign-up/',views.signup ,name='sign-up'),

]