from django.views.generic.base import TemplateView


class SettingsView(TemplateView):
    template_name = 'profile_app/settings.html'