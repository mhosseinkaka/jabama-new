from django.urls import path
from .views import boomgardi

urlpatterns = [
    path("<str:type>",boomgardi)
]