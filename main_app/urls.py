from django.urls import path
from . import views
app_name = 'main_app'


urlpatterns = [
    path('index2/',views.index2 ,name='index2'),
    path('course/<int:id>/',views.course,name='course'),
    path('event/<int:id>/',views.event ,name='event'),
    path('events/',views.events ,name='events'),
    path('search/',views.search ,name='search'),

]