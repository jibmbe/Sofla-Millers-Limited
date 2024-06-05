from django.contrib import admin

from .models import ProductionRecord

@admin.register(ProductionRecord)
class ProductionRecordAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'quantity_produced', 'production_date')