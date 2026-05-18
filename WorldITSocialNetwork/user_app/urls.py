from django.urls import path
from .views import AuthTemplateView
from .endpoints import RegisterView, LoginView, ConfirmEmailView
from .views import LogoutView


urlpatterns = [
    path(route='', view=AuthTemplateView.as_view(), name='user_app.index'),
    
    path(route='register/', view=RegisterView.as_view(), name='user_app.register'),
    path(route='login/', view=LoginView.as_view(), name='user_app.login'),
    path(route='logout/', view= LogoutView.as_view(), name='user_app.logout'),
    path(route='confirm-email/', view=ConfirmEmailView.as_view(), name='user_app.confirm_email'),
]
