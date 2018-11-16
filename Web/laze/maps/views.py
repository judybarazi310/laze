from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class mapsView(TemplateView):
    template_name = "mapview.html"
    def get(self, request):
        return render(request, self.template_name)
        

