"""
Представления приложения IMAGE_UPLOAD.
"""
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView

from .models import Image


class ImageUploadView(CreateView):
    """
    Представление для загрузки картинки.
    """
    model = Image
    fields = ['image']
    template_name = 'image_upload/upload.html'
    success_url = reverse_lazy('image_list')


class ImageListView(ListView):
    """
    Представление списка картинок.
    """
    model = Image
    template_name = 'image_upload/list.html'
    context_object_name = 'images'


class ImageDetailView(DetailView):
    """
    Представление конкретной картинки.
    """
    model = Image
    template_name = 'image_upload/detail.html'
    context_object_name = 'image'
