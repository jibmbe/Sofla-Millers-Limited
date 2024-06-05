from django.shortcuts import render

from .models import PriceCatalogue

def price_catalogue_list(request):
    price_catalogue_items = PriceCatalogue.objects.all()
    return render(request, 'price_catalogue/price_catalogue_list.html', {'price_catalogue_items': price_catalogue_items})
