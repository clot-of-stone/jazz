from django.shortcuts import render, redirect
from .models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort_order = request.GET.get('sort')
    sort_types = {
        'name': 'name',
        'min_price': 'price',
        'max_price': '-price',
    }
    if sort_order:
        context = Phone.objects.all().order_by(sort_types[sort_order])
    else:
        context = Phone.objects.all()
    return render(request, template, {'phones': context})


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    context = {'phone': phone}
    return render(request, template, context)
