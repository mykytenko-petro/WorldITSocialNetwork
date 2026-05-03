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
            raise forms.ValidationError('Користувач с таким email вже є')
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
        widget= forms.EmailInput(attrs= {'placeholder': 'you@example.com', 'autocomplete':"email"})
    )
    password = forms.CharField(
        label='Пароль',
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
        if not User.objects.filter(email= email).exists():
            raise forms.ValidationError('Користувач з таким email вже є')
        return email
    
class ConfirmEmailForm(forms.Form):
    email = forms.CharField(widget=forms.HiddenInput())

    number1 = forms.CharField(
        widget= forms.TextInput(attrs= {'placeholder': '___'}),
        max_length=1, min_length=1, required=True
    )
    number2 = forms.CharField(
        widget= forms.TextInput(attrs= {'placeholder': '___'}),
        max_length=1, min_length=1, required=True
    )
    number3 = forms.CharField(
        widget= forms.TextInput(attrs= {'placeholder': '___'}),
        max_length=1, min_length=1, required=True
    )
    number4 = forms.CharField(
        widget= forms.TextInput(attrs= {'placeholder': '___'}),
        max_length=1, min_length=1, required=True
    )
    number5 = forms.CharField(
        widget= forms.TextInput(attrs= {'placeholder': '___'}),
        max_length=1, min_length=1, required=True
    )
    number6 = forms.CharField(
        widget= forms.TextInput(attrs= {'placeholder': '___'}),
        max_length=1, min_length=1, required=True
    )
    
    def clean(self):
        cleaned_data = super().clean().copy()
        cleaned_data.pop("email")
        
        if len(cleaned_data) != 6:
            raise forms.ValidationError('Цифр має бути шість')

        for value in cleaned_data.values():
            if not value.isdigit():
                raise forms.ValidationError('Це не цифра')
            
        return self.cleaned_data
    
    @property
    def code(self):
        cleaned_data = super().clean().copy()
        cleaned_data.pop("email")
        
        return int("".join(cleaned_data.values()))