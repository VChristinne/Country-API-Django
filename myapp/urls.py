from django.contrib import admin
from django.urls import path
from .views import get_country_info, home_view
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('country-info/', get_country_info, name='country_info'),
    path('', home_view, name='home'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
