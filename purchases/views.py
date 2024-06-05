from django.shortcuts import render

from .models import Purchase

def purchase_list(request):
    purchases = Purchase.objects.all()
    return render(request, 'purchases/purchase_list.html', {'purchases': purchases})
