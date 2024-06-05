from django.contrib import admin

from .models import PriceCatalogue

@admin.register(PriceCatalogue)
class PriceCatalogueAdmin(admin.ModelAdmin):
    list_display = ('item_name', 'unit_price', 'effective_date')