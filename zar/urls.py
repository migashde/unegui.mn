from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from category import views

urlpatterns = [
    path("", views.index, name="index"),
    path('admin/', admin.site.urls),
]

# Correct way to serve media and static files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
