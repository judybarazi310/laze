from django.conf.urls import url
from django.contrib.auth import views as auth_views
from .views import register

urlpatterns = [
	url(r'^login/$', auth_views.LoginView.as_view(template_name='login.html')),
	url(r'^logout/$', auth_views.LogoutView.as_view()),
	url(r'^register/$', register),
]