from django.contrib import admin
from .models import DashboardMetrics

@admin.register(DashboardMetrics)
class DashboardMetricsAdmin(admin.ModelAdmin):
    list_display = (
        'total_purchases',
        'total_inventory_items',
        'total_price_catalogue_items',
        'total_production_records',
        'total_customers',
        'total_sales',
        'total_employees',
        'total_expenses',
        'total_reports',
        'total_suppliers',
        'total_stock_items',
        'avg_aflatoxin_before',
        'avg_aflatoxin_after',
        'avg_moisture_content',
    )
