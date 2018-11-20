from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import forms
from .forms import PinForm


# Create your views here.

def maps_view(request):
    if request.method == 'POST':
        form = PinForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/')

    else:
        form = PinForm()

    return render(request, 'maps.html', {'form': form})
