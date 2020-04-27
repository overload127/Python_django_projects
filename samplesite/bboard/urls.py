from django.urls import path

from .views import index, index2

urlpatterns = [
    path('2', index),
    path('', index2),
]
