"""
Настройки admin-панели приложения IMAGE_UPLOAD.
"""
from django.contrib import admin

from .models import Image


admin.site.register(Image)
