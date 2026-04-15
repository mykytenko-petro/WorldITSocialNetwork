# from django.shortcuts import render

# Create your views here.
# def render_home_app(request):
#     return render(template_name= "home_app/home.html", request= request)

from django.views.generic.base import TemplateView


class HomeView(TemplateView):
    template_name = "home_app/home.html"