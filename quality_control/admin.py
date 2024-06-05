from django.contrib import admin
from .models import QualityControlRecord

@admin.register(QualityControlRecord)
class QualityControlRecordAdmin(admin.ModelAdmin):
    list_display = ('date', 'aflatoxin_before_milling', 'aflatoxin_after_milling', 'moisture_content', 'number_of_bags', 'supplier')
    search_fields = ('date', 'supplier__name')
    list_filter = ('supplier',)

