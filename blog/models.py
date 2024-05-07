from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    name = models.CharField(max_length=255)
    password = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="blog_posts"
    )
    phone = models.IntegerField(null=True)
    birth = models.DateField(null=True)

    def __str__(self):
        return self.name


class user(models.Model):
    name = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="user"
    )
    appointment = models.DateTimeField(null=True)
    event = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="appointment"
    )
    def __str__(self):
        return f"you have apointment {self.name}"

