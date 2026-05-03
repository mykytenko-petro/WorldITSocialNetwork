from django.urls import path

from .views import HomeView
from .endpoints import ProfileDetailView


urlpatterns = [
    path(route="", view=HomeView.as_view(), name='home_app'),

    path(route="complete-profile/", view=ProfileDetailView.as_view(), name='complete_profile')
]