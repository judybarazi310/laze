from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import forms
from .forms import PinForm


# Create your views here.


class MapsView(TemplateView):
    template_name = "maps.html"

    def get(self, request):
        return render(request, self.template_name)

    def createPin(request):
        if request.method == 'POST':
            form = PinForm(request.POST)

            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=raw_password)
                login(request, user)

                return redirect('/')

        else:
            form = RegisterForm()

        return render(request, 'register.html', {'form': form})
