from django.views.generic.base import TemplateView
# Create your views here.
class PublicationsView(TemplateView):
    template_name = 'publications_app/publications.html'