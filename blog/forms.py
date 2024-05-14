from django import forms
from .models import userInfo
from django.conf import settings


class userform(forms.ModelForm): 
    date = forms.DateField(widget=forms.DateInput(attrs={
        'id': 'datePicker', 'class': 'form-control', 'type': 'date'}))

    name_of_the_pet = forms.CharField(widget=forms.TextInput(
                         attrs={'id': 'fullName', 'class': 'form-control',
                                'type': 'text', }))

    time = forms.TimeField(widget=forms.TimeInput(attrs={
        'id': 'Time', 'class': 'form-control', 'type': 'time',
        'step': '3600'}))

    class Meta:
        model = userInfo
        fields = ['time', 'date']
