from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class userInfo(models.Model):
  kind_of_the_pet = models.CharField(max_length=50, null=False, blank=False)
  appointment = models.DateField(blank=False, null=False)
  time = models.DateField(blank=False, null=False)
  text = models.TextField(blank=True)

  def __str__(self):
    return self.kind_of_the_pet
