from django.http import  JsonResponse
import json

def cities(request):
    citiesJSON = json.load(open('static/json/cities.json'))
    return JsonResponse(citiesJSON)