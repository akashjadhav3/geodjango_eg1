from django.shortcuts import render
from .models import Incidences
from django.core.serializers import serialize
from django.http import HttpResponse

def incidence_database(request):
    cities_as_geojson=serialize('geojson', Incidences.objects.all())
    return HttpResponse(cities_as_geojson, content_type='json')
