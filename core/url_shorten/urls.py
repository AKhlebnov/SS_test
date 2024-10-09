"""
Маршруты приложения URL_SHORTEN.
"""
from django.urls import path

from .views import UrlCreateView, UrlListView

urlpatterns = [
    path('create/', UrlCreateView.as_view(), name='create_url'),
    path('urls/', UrlListView.as_view(), name='url_list'),
]
