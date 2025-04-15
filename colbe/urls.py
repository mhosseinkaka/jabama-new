from django.urls import path
from colbe.views import CottageList, CottageCreateView, CottageRUDview

urlpatterns = [
    path("colbe-list/", CottageList.as_view()), 
    path("colbe-add/", CottageCreateView.as_view()),
    path("colbe-rud/<int:pk>/", CottageRUDview.as_view())
]