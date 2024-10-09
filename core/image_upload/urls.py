"""
Маршруты приложения IMAGE_UPLOAD.
"""
from django.urls import path

from .views import ImageUploadView, ImageListView, ImageDetailView

urlpatterns = [
    path('upload/', ImageUploadView.as_view(), name='upload_image'),
    path('images/', ImageListView.as_view(), name='image_list'),
    path('images/<int:pk>/', ImageDetailView.as_view(), name='image_detail'),
]
