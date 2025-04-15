from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from aparteman.models import Place
from aparteman.serializers import ApartemanListSerializer, ApartemanSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
# Create your views here.     


class ApartemanList(ListAPIView):
    queryset = Place.objects.all()
    serializer_class = ApartemanListSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['has_pool', 'is_beachfront', 'is_for_parties', 'status']
    search_fields = ['name', 'owner', 'location', 'status', 'price']

class ApartemanCreateView(CreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Place.objects.all()
    serializer_class = ApartemanSerializer

class ApartemanRUDview(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Place.objects.all()
    serializer_class = ApartemanSerializer
    