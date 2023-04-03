from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
from django.conf import settings
import csv


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stops(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    with open(settings.BUS_STATION_CSV, encoding='utf-8') as database_file:
        database = csv.DictReader(database_file)
        all_stops = [row for row in database]
    page_number = int(request.GET.get('page', 1))
    paginator_obj = Paginator(all_stops, 10)
    page = paginator_obj.get_page(page_number)
    bus_stations = paginator_obj.page(page_number).object_list
    context = {
        'bus_stations': bus_stations,
        'page': page,
    }

    # context = {
    # #     'bus_stations': ...,
    # #     'page': ...,
    # }
    return render(request, 'stations/index.html', context)
