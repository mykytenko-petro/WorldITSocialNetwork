from django.urls import path

from .views import PostsView
from .endpoints import PostCreationView


urlpatterns = [
    path('', PostsView.as_view(), name='post_app.index'),
    path('post_creation/', PostCreationView.as_view(), name='post_app.post_creation'),
]