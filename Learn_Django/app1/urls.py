from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('about/', about, name="about"),
    path('service/', service, name="service"),
    path('contact/', contact, name="contact"),
    path('time/', getTime, name='time'),
    path('greet/', helloBoloHello, name='greet')
]
