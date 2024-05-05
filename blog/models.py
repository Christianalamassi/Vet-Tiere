from django.db import models

# Create your models here.
class patient(models.Model):
    name = models.CharField(max_length=50, unique=True)
    type = models.CharField(max_length=50, unique=True)
   # date_of_birth

    def __str__(self):
        return self.name