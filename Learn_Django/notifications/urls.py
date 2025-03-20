from django.urls import path
from .views import *

urlpatterns = [
    path('getnotifications/<p_user_class>/<p_user_id>', get_notifications, name='get_notifications'),
    path('addnotification/', add_notification, name='add_notification'),
    path('getcsrftoken/', my_get_csrf_token, name='get_csrf_token'),
]
