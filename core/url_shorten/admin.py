"""
Настройки admin-панели приложения URL_SHORTEN.
"""
from django.contrib import admin

from .models import Url


admin.site.register(Url)
