from django.urls import path
from .views import AuthTemplateView, RegisterView


urlpatterns = [
    path(route='', view=AuthTemplateView.as_view(), name='auth'),
    path(route='register/', view=RegisterView.as_view(), name='register'),
    # path(route='login/', view=AuthTemplateView.as_view(), name='login'),
    # path(route='confirm-email/', view=AuthTemplateView.as_view(), name='confirm-email'),
]
