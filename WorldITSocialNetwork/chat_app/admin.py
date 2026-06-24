from django.contrib import admin

from .models import Chat, Message, MessageImage


admin.site.register([
    Chat,
    Message,
    MessageImage
])