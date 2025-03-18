from django.urls import path
from .views import villas_beachfront, villas_party_friendly, villas_pet_friendly, villas_with_entertainment, villas_with_pool


urlpatterns = [
    path("villabeachfront/", villas_beachfront),
    path("villaparty/", villas_party_friendly),
    path("villapet/", villas_pet_friendly),
    path("villa/", villas_with_entertainment),
    path("villapooli/", villas_with_pool),
]
