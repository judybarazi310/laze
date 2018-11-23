from django.conf.urls import url
from django.urls import path

from .views import maps_view, delete_pin, save_location

app_name = "maps"
urlpatterns = [
    url(r'^$', maps_view, name="home"),
    url(r'^search/$', maps_view, name="search_map"),
    path(r'delete/<int:id>/', delete_pin, name="delete_pin"),
    url(r'^save-location/$', save_location, name="save_location"),
]