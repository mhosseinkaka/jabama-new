from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
def boomgardi(request, type):
    data = {
        "kane-gilani": [
            {
                "name": "خانه در گیلان",
                "price": 200000
            },
            {
                "name": "خانه در گیلان",
                "price": 200000
            }
        ],
        "karvansara": [
            {
                "name": "کاروان سرای ممد اینا",
                "price": 2000
            },
            {
                "name": "کاروان سرای علی اینا",
                "price": 2000
            },
        ]
    }
    
    types = ["kane-gilani", "karvansara", "del-shaliz", "khane-tarikhi", "meditaraneh", "sargarmi"]
    
    # Check if the provided type is valid
    if type in types:
        return render(request, "boomgardi.html", context={"type": type, "data": data.get(type, [])})
    else:
        return HttpResponse(f"Not a valid type, available types: {', '.join(types)}")
