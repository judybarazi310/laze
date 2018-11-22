from django.shortcuts import render, redirect, get_object_or_404

from .forms import PinForm
from .models import Pin


# Create your views here.

def maps_view(request, **kwargs):  # TODO create food_pin_list
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
        # temporary
        latlng_pins = Pin.objects.all().exclude(latitude="None")

        render_parameters = {'form': form, 'food_pin_list': food_pin_list, 'study_pin_list': study_pin_list,
                             'parking_pin_list': parking_pin_list, 'info_pin_list': info_pin_list,
                             'latlng_pins': latlng_pins}

        render_parameters["search_text"] = request.GET.get("search_text", None)
        if (render_parameters["search_text"] is not None):
            render_parameters["search_results"] = Pin.objects.filter(title__icontains=render_parameters["search_text"])

    return render(request, 'maps.html', render_parameters)


def delete_pin(request, id):
    pin = get_object_or_404(Pin, id=id)
    pin.delete()
    return redirect('/')
