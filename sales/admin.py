from django.contrib import admin

from .models import Sale

@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ('customer', 'item_name', 'quantity_sold', 'unit_price', 'sale_date')