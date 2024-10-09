"""
Представления приложения URL_SHORTEN.
"""
import random
import string

from django.views.generic import CreateView, ListView

from .models import Url


class UrlCreateView(CreateView):
    """
    Представление создания короткой ссылки.
    """
    model = Url
    fields = ['original_url']
    template_name = 'url_shorten/create.html'
    success_url = '/urls/'

    def form_valid(self, form):
        form.instance.short_url = ''.join(
            random.choices(string.ascii_letters + string.digits, k=6)
        )
        return super().form_valid(form)


class UrlListView(ListView):
    """
    Представление списка ссылок.
    """
    model = Url
    template_name = 'url_shorten/list.html'
    context_object_name = 'urls'
