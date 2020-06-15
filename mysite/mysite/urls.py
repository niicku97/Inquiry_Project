
from django.contrib import admin
from django.urls import path
from inquiry.views import index
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
]


from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)