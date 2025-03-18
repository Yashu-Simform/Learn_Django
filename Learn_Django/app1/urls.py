from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="project_home"),
    path('about/', about, name="about"),
    path('service/', service, name="service"),
    path('contact/', contact, name="contact"),
    path('time/', getTime, name='time'),
    path('greet/', helloBoloHello, name='greet'),
    path('login/', login_options, name='login'),
]
