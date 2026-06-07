from django.db import models
from django.conf import settings

class Profile(models.Model):
    # Користувач чий профіль (Зв'язок один до одного)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='profile'
    )
    
    # Зображення підпису користувача: blank=True, null=True
    signature = models.ImageField(
        upload_to='signatures/',
        blank=True,
        null=True
    )
    
    # Дата народження: blank=True, null=True
    birth_date = models.DateField(
        blank=True,
        null=True
    )
    
    # Аватарка профілю
    avatar = models.ImageField(
        upload_to='avatars/',
        blank=True,
        null=True
    )
    
    # Псевдонім користувача: max_length = 50
    # (Примітка: якщо це унікальне поле для авторизації чи відображення, можна додати unique=True)
    pseudonym = models.CharField(
        max_length=50,
        blank=True,
        null=True
    )
    
    # Чи використовується підпис зображенням
    is_image_signature = models.BooleanField(
        default=False
    )
    
    # Чи використовується підпис текстом (псевдонімом)
    is_text_signature = models.BooleanField(
        default=False
    )

    def __str__(self):
        return f"Profile for {self.user.username}"