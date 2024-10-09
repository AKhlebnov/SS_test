"""
Модели приложения URL_SHORTEN.
"""
from django.db import models


class Url(models.Model):
    """
    Модель ссылки.
    """
    original_url = models.URLField()
    short_url = models.CharField(max_length=6, unique=True)

    def __str__(self):
        return self.original_url
