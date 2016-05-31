from django.http import  JsonResponse, HttpRequest
import json, sqlite3
from . import models

def cities(request):
    citiesJSON = json.load(open('static/json/cities.json'))
    return JsonResponse(citiesJSON)

def markers(request):
    print(request)
    return JsonResponse(get_markers(), safe=False);


def get_markers():
    cities = list(models.City.objects.all().exclude(lat__isnull=True).values())
    return cities;