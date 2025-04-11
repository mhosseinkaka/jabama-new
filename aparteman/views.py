
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from aparteman.models import Place
from aparteman.serializers import ApartemanListSerializer, ApartemanSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
# Create your views here.     


class ApartemanList(ListAPIView):
    queryset = Place.objects.all()
    serializer_class = ApartemanListSerializer

class ApartemanCreateView(CreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Place.objects.all()
    serializer_class = ApartemanSerializer

class ApartemanRUDview(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Place.objects.all()
    serializer_class = ApartemanSerializer
    