from django.forms import ModelForm, HiddenInput
from .models import Pin

class PinForm(ModelForm):
    class Meta:
        model = Pin
        fields = ('title', 'description', 'category', 'latitude', 'longitude')
        widgets = {
            'latitude': HiddenInput(),
            'longitude': HiddenInput(),
        }
