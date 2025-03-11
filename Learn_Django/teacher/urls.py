from django.urls import path, include, reverse
from .views import teacher_home

urlpatterns = [
    path('', teacher_home, name="home"),
    # path('addcourse/', include('course.urls'))
]
