from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.exceptions import ValidationError

class UserInfo(models.Model):
      """Model for booking system"""
      time_options = (
            ("8:00 o'clock", "8:00 o'clock"),
            ("09:00 o'clock", "9:00 o'clock"),
            ("10:00 o'clock", "10:00 o'clock"),
            ("11:00 o'clock", "11:00 o'clock"),
            ("12:00 o'clock", "12:00 o'clock"),
            ("13:00 o'clock", "13:00 o'clock"),
            ("14:00 o'clock", "14:00 o'clock")
      )
      user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
      pet_name = models.CharField(max_length=50, null=False, blank=False)
      date = models.DateField(blank=False)
      oclock = models.CharField(choices=time_options, max_length=20, null=False, blank=False)
      text = models.TextField(blank=True)

      def delete_appointment(self):
            self.delete()

      class Meta:
            ordering = ['date']

      def __str__(self):
            return f'{self.user}: {self.date} at {self.oclock}'


      
    
      # This line will render error when the user tries to book more than one appointment
      def clean(self, *args, **kwargs):
      
            if not self.pk and UserInfo.objects.exists():
                  
                  raise ValidationError(
                  "It seems that You have already booked an appointment.You can have one appointment at the time"
                  )

                  """
                  this won't save any data only to update existing date
                  """
                  return None

            return super(UserInfo, self).save(*args, **kwargs)