from django.urls import path

from .views import HomeView


urlpatterns = [
    path(route="", view=HomeView.as_view(), name='home_app')
]