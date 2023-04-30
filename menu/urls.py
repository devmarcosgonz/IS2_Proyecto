from django.urls import path, include
from .views import *

urlpatterns = [
    path('', Login.as_view(), name='login'),
    path('logout', Logout.as_view(), name='logout'),
    path('main', Main.as_view(), name='main'),
]