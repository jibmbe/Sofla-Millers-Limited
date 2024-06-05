from django.shortcuts import render

from .models import Sale

def sale_list(request):
    sales = Sale.objects.all()
    return render(request, 'sales/sale_list.html', {'sales': sales})
