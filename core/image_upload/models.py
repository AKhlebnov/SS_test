"""
Модели приложения IMAGE_UPLOAD.
"""
from django.db import models


class Image(models.Model):
    """
    Модель картинки.
    """
    image = models.ImageField(upload_to='images/')
