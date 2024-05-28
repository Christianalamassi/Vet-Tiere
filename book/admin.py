from django.contrib import admin
from .models import UserInfo


@admin.register(UserInfo)
class user_appointment(admin.ModelAdmin):
    list_display = (
        'user', 'pet_name', 'date', 'oclock',
        )
    search_fields = ['user', 'pet_name']
    list_filter = ('date',)
