from django.urls import path
from .views import AuthTemplateView
from .endpoints import RegisterView, LoginView

urlpatterns = [
    path(route='', view=AuthTemplateView.as_view(), name='auth'),
    
    path(route='register/', view=RegisterView.as_view(), name='register'),
    path(route='login/', view=LoginView.as_view(), name='login'),
    path(route='confirm-email/', view=AuthTemplateView.as_view(), name='confirm-email'),
]
