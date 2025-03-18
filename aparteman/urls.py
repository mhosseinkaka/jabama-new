from django.urls import path
from .views import aparteman_view_royayee,aparteman_sargarmi

urlpatterns = [
    path("view-royayee", aparteman_view_royayee),
    path("sargarmi", aparteman_sargarmi),
]