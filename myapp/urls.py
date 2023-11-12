from django.contrib import admin
from django.urls import path, include
from .views import get_country_info, home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('country-info/', get_country_info, name='country_info'),
    path('', home_view, name='home'),
]
