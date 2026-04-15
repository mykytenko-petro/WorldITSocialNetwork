from django.views.generic.base import TemplateView
# Create your views here.
class SettingsView(TemplateView):
    template_name = 'settings_app/settings.html'