from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import forms
# Create your views here.


class MapsView(TemplateView):
    template_name = "maps.html"


    def get(self, request):
        return render(request, self.template_name)


class CreatePinView(CreateView):
    form_class = forms

