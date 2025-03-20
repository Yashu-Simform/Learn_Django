from django.db import models

# Create your models here.
class Notification(models.Model):
    user_class = models.CharField(verbose_name='user_class',max_length=255, blank=False, null=False)
    user_id = models.CharField(verbose_name='user_id', max_length=180, blank=False, null=False)
    title = models.CharField(verbose_name='title', max_length=255)
    message = models.TextField(verbose_name='message')
    seen = models.BooleanField(verbose_name='seen', default=False)