from django.urls import path

from .views import AuthorizationView, RegistrationView


urlpatterns = [
    path("regisration/", view=RegistrationView.as_view(), name='registration_app'),
    path("authorization/", view=AuthorizationView.as_view(), name='authorization_app')
]