from django.urls import path
from . import views
app_name = 'accounts'


urlpatterns = [
    path('sign-in/',views.signin ,name='sign-in'),
    path('sign-up/',views.signup ,name='sign-up'),
    # path('sign-out',views.signout ,name='sign-out'),

]