from django.urls import path
from .views import add_course

urlpatterns = [
    path('addcourse/', add_course, name='add_course')
]
