from django.views.generic.base import TemplateView

# Create your views here.
class ChatView(TemplateView):
    template_name = 'chat_app/chat.html'