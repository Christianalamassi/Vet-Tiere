from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    name = models.CharField(max_length=255)
    birth = models.DateField(null=True)

    def __str__(self):
        return self.name


