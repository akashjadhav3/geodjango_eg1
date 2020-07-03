from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from django.views.generic import TemplateView
from djgeojson.views import GeoJSONLayerView

from .models import MushroomSpot
from . import views


urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('data/', GeoJSONLayerView.as_view(model=MushroomSpot, properties=('title', 'description', 'picture_url')), name='data'),
    path('data.g/',views.incidence_database, name='data2')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)