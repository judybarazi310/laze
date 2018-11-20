from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import forms
from .forms import PinForm
from .models import Pin


# Create your views here.

def maps_view(request):  # TODO create food_pin_list
    if request.method == 'POST':
        form = PinForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/')

    else:
        form = PinForm()
        food_pin_list = Pin.objects.filter(category="FOOD")
        study_pin_list = Pin.objects.filter(category="STY")
        parking_pin_list = Pin.objects.filter(category="VEHP")
        info_pin_list = Pin.objects.filter(category="INFO")
    return render(request, 'maps.html', {'form': form, 'food_pin_list': food_pin_list, 'study_pin_list': study_pin_list,
                                         'parking_pin_list': parking_pin_list, 'info_pin_list': info_pin_list})
