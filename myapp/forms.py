from django import forms
from .models import *

class userdetialsform(forms.ModelForm):
    class Meta:
        model=userdetails
        fields='__all__'