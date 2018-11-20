from django.forms import ModelForm
from maps.models import Pin


class PinForm(ModelForm):
    class Meta:
        model = Pin
