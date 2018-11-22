from django.conf.urls import url

from .views import maps_view, delete_pin

app_name = "maps"
urlpatterns = [
    url(r'$', maps_view, name="home"),
    url(r'^search/$', maps_view, name="search_map"),
    url(r'^delete/id=(?P<id>[\d]+)', delete_pin, name="delete_pin"),
]
