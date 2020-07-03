from leaflet.admin import LeafletGeoAdmin
from django.contrib import admin

from . import models as mushrooms_models

from .models import Incidences



class IncidencesAdmin(LeafletGeoAdmin):
    pass
    # list_display = ('name', 'location') # user for show column name

admin.site.register(Incidences, IncidencesAdmin)


admin.site.register(mushrooms_models.MushroomSpot, LeafletGeoAdmin)