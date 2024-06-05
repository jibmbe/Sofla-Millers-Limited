from django.contrib import admin
from .models import Product, Stock, StockItem, Transaction

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'unit')

class StockAdmin(admin.ModelAdmin):
    list_display = ('product', 'opening_stock', 'closing_stock', 'available_stock', 'date')
    list_filter = ('date', 'product')
    search_fields = ('product__name',)

class TransactionAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity', 'transaction_type', 'transaction_date')
    list_filter = ('transaction_date', 'transaction_type', 'product')
    search_fields = ('product__name',)

admin.site.register(Product, ProductAdmin)
admin.site.register(Stock, StockAdmin)  
admin.site.register(Transaction, TransactionAdmin)
admin.site.register(StockItem)
