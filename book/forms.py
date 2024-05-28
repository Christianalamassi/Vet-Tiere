from django import forms
from .models import UserInfo
from django.utils import timezone
from django.core.exceptions import ValidationError

class UserForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ['pet_name', 'date', 'oclock', 'text']
    
    date = forms.DateField(widget=forms.DateInput(attrs={
        'id': 'datePicker', 'class': 'form-control', 'type': 'date'
    }))
    
    pet_name = forms.CharField(widget=forms.TextInput(attrs={
        'id': 'fullName', 'class': 'form-control', 'type': 'text'
    }))
    
    oclock = forms.ChoiceField(choices=UserInfo.time_options, widget=forms.Select(attrs={
        'id': 'Time', 'class': 'form-control'
    }))
    
    text = forms.CharField(widget=forms.Textarea(attrs={
        'id': 'text', 'class': 'form-control', 'rows': 3
    }), required=False)

    # Access the request in the form
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(UserForm, self).__init__(*args, **kwargs)
    
    # Raising date error for invalid time
    def clean_date(self):
        date = self.cleaned_data.get('date')
        if date < timezone.now().date():
            raise ValidationError('Please make sure that your date in the future.')
        return date

    #Raising  error for making more than one appointment at a time
    def clean(self):
        cleaned_data = super().clean()
        if self.request and self.request.user:
            user = self.request.user
            if UserInfo.objects.filter(user=user).exists():
                raise forms.ValidationError("You already have a booking. Users can have one booking at a time.")
        return cleaned_data


    #Raising error for getting two users the same appointment
    def clean_oclock(self):
        oclock = self.cleaned_data.get('oclock')
        date = self.cleaned_data.get('date')
        if UserInfo.objects.filter(oclock=oclock).exists() and UserInfo.objects.filter(date=date).exists():
                raise forms.ValidationError("Oops! This appointment has been taken")
        return oclock