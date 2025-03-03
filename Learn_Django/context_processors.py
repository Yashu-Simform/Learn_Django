# app1/context_processors.py

from django.conf import settings

def global_settings(request):
    return {
        'BASE_URL': settings.BASE_URL,
        'PORT': settings.PORT,
    }
