from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class userInfo(models.Model):
  name_of_the_pet = models.CharField(max_length=50)
  appointment = models.DateField(blank=True, null=True)
  time = models.DateField(blank=True, null=True)
  text = models.TextField(blank=True)

  def __str__(self):
    return self.appointment.count()

  def __str__(self):
    return self.time.count()
