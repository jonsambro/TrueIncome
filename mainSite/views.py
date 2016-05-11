from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
import os


def index(request):
    return HttpResponse(render(request, 'mainSite/index.html'))