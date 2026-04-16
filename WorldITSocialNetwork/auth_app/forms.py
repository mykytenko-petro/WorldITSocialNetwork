from django import forms
from .models import Post
from django.db import models
from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(),
    )
    password_confirm = forms.CharField(
        widget=forms.PasswordInput(),
    )
    email = forms.CharField(
        widget=forms.EmailInput()
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password_confirm']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError('Паролі не співпадають')
        return cleaned_data


class AuthorizationForm(forms.ModelForm):
    email = forms.CharField(
        widget=forms.EmailField()
    )
    password = forms.CharField(
        widget= forms.PasswordInput()
    )
    password_confirm  = forms.CharField(
        widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ['email', 'password', 'password_confirm']
        
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError('Паролі не співпадають')
        return cleaned_data