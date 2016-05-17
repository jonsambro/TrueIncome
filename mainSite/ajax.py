from django.http import  JsonResponse, HttpRequest
import json

def cities(request):
    citiesJSON = json.load(open('static/json/cities.json'))
    return JsonResponse(citiesJSON)

def markers(request):
    print(request)
    return JsonResponse(json.load(open('static/json/cities.json')));