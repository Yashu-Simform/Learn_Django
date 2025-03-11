from django.urls import path, include, reverse
from .views import home

urlpatterns = [
    path('', home, name="home"),
    # path('addcourse/', include('course.urls'))
]
