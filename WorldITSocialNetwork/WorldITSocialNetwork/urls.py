from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from debug_toolbar.toolbar import debug_toolbar_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path(route='', view=include('home_app.urls')),
    path(route='profile/', view=include('profile_app.urls')),
    path(route='post/', view=include('post_app.urls')),
    path(route='user/', view=include('user_app.urls')),
    path(route='chat/', view=include('chat_app.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += debug_toolbar_urls()
