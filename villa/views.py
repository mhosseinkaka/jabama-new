from django.http.response import JsonResponse
from villa.models import Villa
from django.views.decorators.csrf import csrf_exempt
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from villa.serilaizers import  VillaSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly



def list_villa(request):
    all_villas = Villa.objects.all().values("name","description")
    all_villas = list(all_villas)
    return  JsonResponse(all_villas ,safe=True)


class ListVillaView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Villa.objects.all()
    serializer_class = VillaSerializer
    
    
class CreatVillaView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Villa.objects.all()
    serializer_class = VillaSerializer
    
    
    def perform_create(self, serializer):
        
        serializer.save(
            user = self.request.user
            
        )
    
    
    
    
class RetrieveVillaView(RetrieveAPIView) :
    queryset = Villa.objects.all()
    serializer_class = VillaSerializer

class DeleteVillaView(DestroyAPIView) :
    permission_classes = [IsAdminUser]
    queryset = Villa.objects.all()
    serializer_class = VillaSerializer
    
class UpdateVillaView(UpdateAPIView) :
    queryset = Villa.objects.all()
    serializer_class = VillaSerializer


class CreateListVillaView(ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Villa.objects.all()
    serializer_class = VillaSerializer
    
class RetriveUpdateDeleteVillaView(RetrieveUpdateDestroyAPIView):
    queryset = Villa.objects.all()
    serializer_class = VillaSerializer  


