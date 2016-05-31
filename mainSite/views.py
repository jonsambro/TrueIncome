from django.shortcuts import render
from django.http import HttpResponse
from . import models
import sqlite3, time

def index(request):
    start = time.time()
    area_locations = get_jobs()
    print(len(area_locations))
    end = time.time()
    print(end-start)
    return HttpResponse(render(request, 'mainSite/index.html',
        context={
            'names':"Jonathan Brown and Graeme Crawley",
            'jobs' : area_locations
        }))

def get_jobs():
    connection = sqlite3.connect('incomeDatabase.db')
    c = connection.cursor()
    c.execute('SELECT OCC_CODE, OCC_TITLE FROM city_salaries WHERE AREA="11260" ORDER BY OCC_TITLE');
    locations = c.fetchall()
    c.close();
    return locations;