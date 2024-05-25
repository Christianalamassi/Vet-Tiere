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
    
    def clean_date(self):
        date = self.cleaned_data.get('date')
        if date < timezone.now().date():
            raise ValidationError('The date it has to be in the future.')
        return date