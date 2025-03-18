from django.shortcuts import render
from django.http.response import HttpResponse
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