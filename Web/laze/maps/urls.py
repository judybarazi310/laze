from django.conf.urls import url
from .views import maps_view

urlpatterns = [
    url(r'/$', maps_view, name="map_page"),
    url(r'^search/$', maps_view, name="search map page")
]
