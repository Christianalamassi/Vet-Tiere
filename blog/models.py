from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

class userInfo(models.Model):
  appointment = models.DateField(blank=True, null=True)
  time = models.DateField(blank=True, null=True)

  def __str__(self):
    return self.appointment.count()

  def __str__(self):
    return self.time.count()
