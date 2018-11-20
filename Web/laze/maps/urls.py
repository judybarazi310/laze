from django.conf.urls import url
from .views import MapsView

urlpatterns = [
    url(r'/$', MapsView.as_view(), name="maps"),
    url(r'^ajax/createPin/$', MapsView.createPin, name="create_pin"),
]
