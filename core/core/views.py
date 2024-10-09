"""
Представления CORE.
"""
from django.shortcuts import render


def home_view(request):
    """
    Функция представления главного экрана приложения.
    """
    return render(request, 'index.html')
