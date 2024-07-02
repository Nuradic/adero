from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from app.views import *

urlpatterns = [
    path("", home),
    path("admin/", admin.site.urls),
    path("test/", test),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
