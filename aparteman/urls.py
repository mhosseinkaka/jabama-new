from django.urls import path
from aparteman.views import ApartemanList, ApartemanCreateView, ApartemanRUDview

urlpatterns = [
    path("aparteman-list/", ApartemanList.as_view()), 
    path("aparteman-add/", ApartemanCreateView.as_view()),
    path("aparteman-rud/<int:pk>/", ApartemanRUDview.as_view())
]