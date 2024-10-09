"""
Представления API.
"""
from rest_framework import generics

from image_upload.models import Image
from .serializers import ImageSerializer


class ImageUploadAPI(generics.CreateAPIView):
    """
    Представление для загрузки картинки через API.
    """
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
