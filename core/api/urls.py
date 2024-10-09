"""
Маршруты API.
"""
from django.urls import path

from .views import ImageUploadAPI


urlpatterns = [
    path('upload/', ImageUploadAPI.as_view(), name='api_upload_image'),
]
