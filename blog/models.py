from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


# Create your models here.

class userInfo(models.Model):
  """Model for booking system"""
  time_options = {
("8:00","8:00"),
("09:00","9:00"),
("10:00","10:00"),
("11:00","11:00"),
("12:00","12:00"),
("13:00","13:00"),
("14:00","14:00")
  }
  user =models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True)
  pet_name = models.CharField(max_length=50, null=False, blank=False)
  date = models.DateField(blank=False, null=False)
  time = models.CharField(max_length=7, choices=time_options, null=False, blank=False)
  text = models.TextField(blank=True)
  
  def delete_appointment(self):
        self.delete()

  def __str__(self):
    return self.user

    class Meta:
        ordering = ['pet_name','date', 'time']
