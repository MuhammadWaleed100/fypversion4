from django import forms
from .models import User

class loginForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['uname','em','pas','rad']
