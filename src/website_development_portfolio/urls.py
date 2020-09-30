"""
Project URL Configuration
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='landing'),
    path('projects/', include('main.urls')),
    path('policies/', include('extra.urls'))
]

# Static and media files routing
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
