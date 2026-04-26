from django import forms
from django.contrib.auth import authenticate, get_user_model

User = get_user_model()

class RegisterForm(forms.Form):
    email = forms.EmailField(
        label='Електронна пошта',
        widget= forms.EmailInput(attrs= {'placeholder': 'you@example.com'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs= {'placeholder': 'Введи пароль'}),
        label='Пароль'
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs= {'placeholder': 'Повтори пароль'}),
        label='Підтвердження паролю'
    )
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Пользователь с таким email вже є')
        return email

    def clean(self):
        cleaned_data = super().clean()
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        
        if password and confirm_password and password == confirm_password:
            return cleaned_data
        
        raise forms.ValidationError('Паролі не співпадають')
    
class LoginForm(forms.Form):
    email = forms.EmailField(
        label='Електронна пошта', 
        widget= forms.EmailInput(attrs= {'placeholder': 'you@example.com'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs= {'placeholder': 'Введи пароль'})
    )
    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        if not email:
            return cleaned_data
        if email and password:
            user = authenticate(email=email, password=password)
            if not user:
                raise forms.ValidationError('Невірний пароль')
        return cleaned_data
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email= email).exists():
            raise forms.ValidationError('Користувач з таким email вже є')
    

class ConfirmEmailForm(forms.Form):
    email1 = forms.CharField(max_length=1, min_length=1, required=True)
    email2 = forms.CharField(max_length=1, min_length=1, required=True)
    email3 = forms.CharField(max_length=1, min_length=1, required=True)
    email4 = forms.CharField(max_length=1, min_length=1, required=True)
    email5 = forms.CharField(max_length=1, min_length=1, required=True)
    email6 = forms.CharField(max_length=1, min_length=1, required=True)
    
    def clean(self):
        cleaned_data = super().clean()
        emailconfirm = (
            cleaned_data.get("email1", "") +
            cleaned_data.get("email2", "") +
            cleaned_data.get("email3", "") +
            cleaned_data.get("email4", "") +
            cleaned_data.get("email5", "") +
            cleaned_data.get("email6", "")
        )
        if len(emailconfirm) !=6:
            raise forms.ValidationError("Код невірний")
        return cleaned_data