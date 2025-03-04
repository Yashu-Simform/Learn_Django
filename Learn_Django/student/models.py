from django.db import models

# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField(max_length=255, default='example@gmail.com', unique=True)
    city = models.CharField(max_length=70, default='Junagadh')
    roll_no = models.IntegerField(default = 0, unique=True)