from django.urls import path
from colbe.views import cottage

urlpatterns = [
    path('', cottage)
]