from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class Login(LoginView):
    next_page = reverse_lazy('main')
    template_name = 'login.html'


class Logout(LogoutView):
    next_page = reverse_lazy('login')


class Main(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('login')
    template_name = 'main.html'