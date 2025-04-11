from django.urls import path
from boomgardi.views import CreateListBoomgardiView, RetriveUpdateDeleteBoomgardiView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView



urlpatterns = [
    path('list-create', CreateListBoomgardiView.as_view()),
    path('retrieve-delete-update/<int:pk>', RetriveUpdateDeleteBoomgardiView.as_view()) ,
    path('login', TokenObtainPairView.as_view()) ,
    path('refresh', TokenRefreshView.as_view()) ,
    path('verify' , TokenVerifyView.as_view())
]