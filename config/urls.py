from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from config import settings

urlpatterns = [
    path('admin/', admin.site.urls),  # admin panel url

    # API urls
    path('api/common/', include('common.urls')),
    path('api/tobacco/', include('tobacco.urls')),
    path('api/mix/', include('mix.urls')),
    path('api/lounge/', include('lounge.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
