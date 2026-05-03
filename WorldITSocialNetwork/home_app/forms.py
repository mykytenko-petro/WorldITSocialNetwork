from django import forms
from django.contrib.auth import get_user_model


User = get_user_model()

class ProfileDetailForm(forms.Form):
    author_pseudonym = forms.CharField(
        label="Псевдонім автора",
        widget=forms.TextInput(attrs={"placeholder": "Введіть Псевдонім автора"})
    )
    username = forms.CharField(
        label="Ім’я користувача",
        widget=forms.TextInput(attrs={"placeholder": "@"})
    )

    def clean_author_pseudonym(self):
        return self.cleaned_data['author_pseudonym']
    
    def clean_username(self):
        username = self.cleaned_data['username']
        
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Таке ім'я користувача вже зайняте")
        
        return username