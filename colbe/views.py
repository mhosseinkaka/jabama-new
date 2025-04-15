from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from colbe.models import Place
from colbe.serializers import ColbeListSerializer, ColbeSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

# Create your views here.

class CottageList(ListAPIView):
    queryset = Place.objects.all()
    serializer_class = ColbeListSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['has_pool', 'is_beachfront', 'is_for_parties', 'status']
    search_fields = ['name', 'owner', 'location', 'status', 'price']

class CottageCreateView(CreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Place.objects.all()
    serializer_class = ColbeSerializer

class CottageRUDview(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Place.objects.all()
    serializer_class = ColbeSerializer    