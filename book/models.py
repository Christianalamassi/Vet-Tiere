from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.exceptions import ValidationError

class UserInfo(models.Model):
      """Model for booking system related to :model:`auth.User`."""
      time_options = (
            ("8:00 o'clock", "8:00 o'clock"),
            ("09:00 o'clock", "9:00 o'clock"),
            ("10:00 o'clock", "10:00 o'clock"),
            ("11:00 o'clock", "11:00 o'clock"),
            ("12:00 o'clock", "12:00 o'clock"),
            ("13:00 o'clock", "13:00 o'clock"),
            ("14:00 o'clock", "14:00 o'clock")
      )
      user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
      pet_name = models.CharField(max_length=50, blank=True)
      date = models.DateField()
      oclock = models.CharField(choices=time_options, max_length=20, blank=True)
      text = models.TextField(blank=True)

      def delete_appointment(self):
            self.delete()

      class Meta:
            ordering = ['date','oclock']

      def __str__(self):
            return f'{self.user}: {self.date} at {self.oclock}'

