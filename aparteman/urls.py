from django.urls import path
from .views import aparteman_view_royayee,aparteman_sargarmi, ApartemanList, ApartemanLCView, ApartemanRUDview

urlpatterns = [
    path("view-royayee/", aparteman_view_royayee),
    path("sargarmi/", aparteman_sargarmi),
    path("apateman-list/", ApartemanList.as_view()), 
    path("aprteman-lc/", ApartemanLCView.as_view()),
    path("aparteman-rud/<int:pk>/", ApartemanRUDview.as_view())
]