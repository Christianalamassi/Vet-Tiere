from django import forms
from .models import userInfo
from .forms import ItemForm

class ItemForm(forms.ModelForm): 
    class Meta:
        model = userInfo
        fields = ['time', 'date']
