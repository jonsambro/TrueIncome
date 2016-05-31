from django.http import  JsonResponse, HttpRequest
import json, sqlite3
from . import models

def cities(request):
    citiesJSON = json.load(open('static/json/cities.json'))
    return JsonResponse(citiesJSON)

def markers(request):
    print(request)
    return JsonResponse(get_markers(request.GET.get('OCC_ID','00-0000')), safe=False);


def get_markers(id):
    salaries = models.Salary.objects.filter(occ_code=id, city__lat__isnull=False)
    salaries = list(salaries.values('city__name','city__lat','city__lng','city__costOfLiving','a_median'))
    for x in salaries:
        print(type(x))
        x['name'] = x.pop('city__name')
        x['lat'] = x.pop('city__lat')
        x['lng'] = x.pop('city__lng')
        x['costOfLiving'] = x.pop('city__costOfLiving')
    return salaries;