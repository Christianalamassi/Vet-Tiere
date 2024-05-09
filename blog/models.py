from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class user_info(models.Model):
   Full_name = models.CharField(max_length=255)
   User_name = models.CharField(max_length=255)
   E_mail = models.CharField(max_length=255)
   appointment = models.DateField(null=True)
   def __str__(self):
     return self.name
