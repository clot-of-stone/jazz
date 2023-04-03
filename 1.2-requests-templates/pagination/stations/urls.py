from django.urls import path

from .views import index, bus_stops

urlpatterns = [
    path('', index, name='index'),
    path('bus_stations/', bus_stops, name='bus_stations'),
]
