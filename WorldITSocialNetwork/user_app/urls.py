from django.urls import path
from .views import AuthView, LogoutView
from .endpoints import RegisterView, LoginView, ConfirmEmailView


urlpatterns = [
    # views
    path(route='', view=AuthView.as_view(), name='user_app.index'),
    path(route='logout/', view=LogoutView.as_view(), name='user_app.logout'),
    
    # endpoints
    path(route='register/', view=RegisterView.as_view(), name='user_app.register'),
    path(route='login/', view=LoginView.as_view(), name='user_app.login'),
    path(route='confirm-email/', view=ConfirmEmailView.as_view(), name='user_app.confirm_email'),
]
