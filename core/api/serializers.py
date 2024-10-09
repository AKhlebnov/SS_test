"""
Файл сериализатора для API.
"""
from rest_framework import serializers

from image_upload.models import Image


class ImageSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Image.
    """
    class Meta:
        model = Image
        fields = ['id', 'image']
