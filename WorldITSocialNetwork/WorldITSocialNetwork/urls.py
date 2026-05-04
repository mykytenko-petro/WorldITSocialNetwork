from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path(route='', view=include('home_app.urls')),
    path(route='profile/', view=include('profile_app.urls')),
    path(route='post/', view=include('post_app.urls')),
    path(route='user/', view=include('user_app.urls')),
]
 