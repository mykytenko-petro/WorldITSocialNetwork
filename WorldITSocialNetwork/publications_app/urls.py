from django.urls import path
from .views import PublicationsView

urlpatterns = [
    path('', PublicationsView.as_view(), name='publications_app'),
]