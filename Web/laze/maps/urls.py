from django.conf.urls import url
from .views import maps_view

urlpatterns = [
    url(r'/$', maps_view, name="map_page"),
]
