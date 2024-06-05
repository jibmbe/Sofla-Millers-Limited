# dashboard/views.py
from django.shortcuts import render
from django.utils import timezone
from .models import DashboardMetrics
from suppliers.models import Supplier

def dashboard_view(request):
    date_filter = request.GET.get('date')
    if date_filter:
        metrics = DashboardMetrics.objects.filter(aflatoxin_test_date=date_filter).first()
    else:
        metrics = DashboardMetrics.objects.first()

    daily_summary = {
        'today': timezone.now().date(),
        'total_purchases_today': metrics.total_purchases if metrics else 0,
        'total_sales_today': metrics.total_sales if metrics else 0,
        'total_production_records_today': metrics.total_production_records if metrics else 0,
        'total_bags_today': metrics.total_inventory_items if metrics else 0,  # Replace with actual logic if different
        'suppliers_today': Supplier.objects.all(),  # Replace with actual logic
        'avg_aflatoxin_before': metrics.avg_aflatoxin_before if metrics else 0.0,
        'avg_aflatoxin_after': metrics.avg_aflatoxin_after if metrics else 0.0,
        'avg_moisture_content': metrics.avg_moisture_content if metrics else 0.0,
        'aflatoxin_test_date': metrics.aflatoxin_test_date if metrics else None,
        'moisture_test_date': metrics.moisture_test_date if metrics else None,
    }

    return render(request, 'dashboard/dashboard.html', {'daily_summary': daily_summary})
