from django.urls import path
from .views import (
    AuthView, LogoutView,
    FriendsView, FriendPageView
)
from .endpoints import (
    RegisterView, LoginView, ConfirmEmailView,
)


urlpatterns = [
    # auth
    path(route='auth/', view=AuthView.as_view(), name='user_app.auth'),
    path(route='logout/', view=LogoutView.as_view(), name='user_app.logout'),
    
    path(route='register/', view=RegisterView.as_view(), name='user_app.register'),
    path(route='login/', view=LoginView.as_view(), name='user_app.login'),
    path(route='confirm-email/', view=ConfirmEmailView.as_view(), name='user_app.confirm_email'),
    
    # friend
    path(route='friends/', view=FriendsView.as_view(), name='user_app.friends'),
    path(route='<int:user_id>/', view= FriendPageView.as_view(), name="user_app.friend_page")
]
