from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class PublicationsView(LoginRequiredMixin, TemplateView):
    template_name = 'publications_app/publications.html'