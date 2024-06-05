from django.shortcuts import render

from .models import ProductionRecord

def production_list(request):
    production_records = ProductionRecord.objects.all()
    return render(request, 'production/production_list.html', {'production_records': production_records})
