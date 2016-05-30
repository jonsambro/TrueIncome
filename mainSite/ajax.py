from django.http import  JsonResponse, HttpRequest
import json, sqlite3

def cities(request):
    citiesJSON = json.load(open('static/json/cities.json'))
    return JsonResponse(citiesJSON)

def markers(request):
    print(request)
    return JsonResponse(get_markers(), safe=False);


def get_markers():
    connection = sqlite3.connect('incomeDatabase.db')
    c = connection.cursor()
    c.execute('SELECT AREA_NAME, STATE, LATITUDE, LONGITUDE FROM area_locations WHERE LATITUDE IS NOT NULL AND LONGITUDE IS NOT NULL');
    locations = c.fetchall()
    c.close();
    keys = ['area_name','state','latitude','longitude']
    dicts = [dict(zip(keys, l)) for l in locations]
    print(json.dumps(dicts))
    #locationsJSON = json.loads(dicts)
    return dicts;