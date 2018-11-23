from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import login, authenticate, logout as logout_function
from maps.models import UserLocation

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)

            return redirect('/')
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form, 'title': 'Laze Registration'})

def logout(request):
    if request.user.is_authenticated:
        users = UserLocation.objects.filter(user=request.user)
        
        if users.exists():
            users.delete()

        logout_function(request)

    return redirect('/accounts/login')