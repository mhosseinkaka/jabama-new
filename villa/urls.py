from django.urls import path
from .views import   ListVillaView,CreatVillaView ,CreateListVillaView,UpdateVillaView,DeleteVillaView,RetriveUpdateDeleteVillaView


urlpatterns = [
    path('new-list', ListVillaView.as_view()),
    path('create' ,CreatVillaView.as_view() ),
    path('update/<int:pk>' ,UpdateVillaView.as_view()),
    path('delete/<int:pk>' , DeleteVillaView.as_view()),
    path('create-list' , CreateListVillaView.as_view()),
    path('retrive-update-delete',RetriveUpdateDeleteVillaView.as_view())
]
