from django import forms

from .models import *
class RegisterForm(forms.ModelForm):
    password = forms.CharField(max_length=30,widget=forms.PasswordInput(
        attrs={
        'placeholder':'Enter Password',
    }
    ))
    confirm_password = forms.CharField(max_length=30,widget=forms.PasswordInput(
        attrs={
        'placeholder':'Enter Password',
    }
    ))
    class Meta:
        model = Customer
        fields = '__all__'