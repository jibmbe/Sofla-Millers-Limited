from django.contrib import admin
from .models import Batch, Invoice

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('invoice_number', 'sale', 'issue_date', 'due_date', 'salesperson')
    search_fields = ('invoice_number', 'sale', 'issue_date', 'due_date', 'salesperson__name', 'customer__name')

@admin.register(Batch)
class BatchAdmin(admin.ModelAdmin):
    list_display = ('batch_number', 'description')