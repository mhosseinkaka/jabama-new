from django.http.response import JsonResponse

def villas_with_pool(request):
    data = [
        {
            "name": "Luxury Pool Villa",
            "description": "A stunning villa with a private infinity pool and panoramic views.",
            "rating": 4.8,
            "price_per_night": 350
        },
        {
            "name": "Tropical Oasis Villa",
            "description": "Relax in this tropical villa with a large pool surrounded by lush gardens.",
            "rating": 4.7,
            "price_per_night": 300
        }
    ]
    return JsonResponse(data, safe=False)

def villas_beachfront(request):
    data = [
        {
            "name": "Oceanfront Paradise",
            "description": "Wake up to the sound of waves in this beachfront villa with direct sea access.",
            "rating": 4.9,
            "price_per_night": 400
        },
        {
            "name": "Seaside Retreat",
            "description": "Enjoy breathtaking sunsets from this cozy beachfront villa.",
            "rating": 4.6,
            "price_per_night": 320
        }
    ]
    return JsonResponse(data, safe=False)

def villas_with_entertainment(request):
    data = [
        {
            "name": "Entertainment Haven",
            "description": "This villa features a home theater, game room, and a private pool.",
            "rating": 4.5,
            "price_per_night": 380
        },
        {
            "name": "Fun Villa",
            "description": "Perfect for families, this villa has a cinema room, pool table, and more.",
            "rating": 4.4,
            "price_per_night": 360
        }
    ]
    return JsonResponse(data, safe=False)

def villas_pet_friendly(request):
    data = [
        {
            "name": "Pet-Friendly Retreat",
            "description": "Bring your furry friends to this spacious villa with a large garden.",
            "rating": 4.7,
            "price_per_night": 280
        },
        {
            "name": "Cozy Pet Villa",
            "description": "A cozy villa with a fenced yard, perfect for pets and their owners.",
            "rating": 4.6,
            "price_per_night": 260
        }
    ]
    return JsonResponse(data, safe=False)

def villas_party_friendly(request):
    data = [
        {
            "name": "Party Villa",
            "description": "Host the ultimate party at this villa with a pool, BBQ area, and large open space.",
            "rating": 4.8,
            "price_per_night": 450
        },
        {
            "name": "Celebration Villa",
            "description": "Perfect for big gatherings, this villa has a dance floor and a fully equipped kitchen.",
            "rating": 4.7,
            "price_per_night": 420
        }
    ]
    return JsonResponse(data, safe=False)
