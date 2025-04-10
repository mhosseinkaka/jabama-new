from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from aparteman.models import Place
from aparteman.serializers import ApartemanListSerializer
# Create your views here.     

def aparteman_view_royayee(request):
    data = [
        {
            "name":"آپارتمان در قیطریه",
            "price":1000000
        },
        {
            "name":"آپارتمان در قیطریه",
            "price":1000000
        },
        {
            "name":"آپارتمان در قیطریه",
            "price":1000000
        }
    ]
    return render(request,"aparteman.html",
        context={
                "type":"با ویو رویایی",
                "data":data
                })

class ApartemanList(ListAPIView):
    queryset = Place.objects.all()
    serializer_class = ApartemanListSerializer

class ApartemanLCView(ListCreateAPIView):
    queryset = Place.objects.all()
    serializer_class = ApartemanListSerializer

class ApartemanRUDview(RetrieveUpdateDestroyAPIView):
    queryset = Place.objects.all()
    serializer_class = ApartemanListSerializer

def aparteman_sargarmi(request):
    data = [
        {
            "name":"آپارتمان در نیاوران",
            "price":40000000
        },
        {
            "name":"آپارتمان در نیاوران",
            "price":40000000
        },
        {
            "name":"آپارتمان در نیاوران",
            "price":40000000
        },
        {
            "name":"آپارتمان در نیاوران",
            "price":40000000
        },
    ]
    return render(request,"aparteman.html",
        context={
                "type":"با سرگرمی",
                "data":data
                })