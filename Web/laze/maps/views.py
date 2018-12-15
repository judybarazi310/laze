from django.shortcuts import render, redirect, get_object_or_404

from .forms import PinForm
from .models import Pin, UserLocation
from .controllers import calculate_nearby

from django.http import HttpResponse


def maps_view(request, **kwargs):  
    if request.method == 'POST' and request.user.is_authenticated:
        form = PinForm(request.POST)

        if form.is_valid():
            model=form.save(commit=False)
            model.created_by = request.user
            model.save()
            return redirect('/')

    else:
        calculate_nearby(UserLocation.objects.all(), Pin.objects.all())

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

def save_location(request):
    if request.method == 'POST' and request.user.is_authenticated:
        try:
            latitude = float(request.POST.get('latitude'))
            longitude = float(request.POST.get('longitude'))
        except:
            return HttpResponse('Bad arguments', status=400)

        user = UserLocation.objects.filter(user=request.user)

        if user.exists():
            user = user[0]

            user.latitude = latitude
            user.longitude = longitude

            user.save()
        else:
            UserLocation(latitude=latitude, longitude=longitude, user=request.user).save()

    return HttpResponse(status=200)