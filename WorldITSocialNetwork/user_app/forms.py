from django import forms

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

class LoginForm(forms.Form):
    email = forms.EmailField(
        label='Електронна пошта', 
        widget= forms.EmailInput(attrs= {'placeholder': 'you@example.com'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs= {'placeholder': 'Введи пароль'})
    )

class ConfirmEmailForm(forms.Form):
    code = forms.CharField(
        max_length=6,
        min_length=6,
        widget=forms.TextInput(attrs={
            'class': 'otp-input',
            'placeholder': '······',
            'type': 'text',
            'autocomplete': 'one-time-code', # Помогает автозаполнению из SMS/почты
            'pattern': r'\d{6}', # Подсказка для браузера, что нужны только цифры
        })
    )