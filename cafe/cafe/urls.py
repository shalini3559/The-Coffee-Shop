
from authentication.views import register_page 
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', include('BrewHaven.urls')),
    path('admin/', admin.site.urls),
    path('authentication/',include('authentication.urls')),
    path('register/',register_page, name='register'),
    ] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


