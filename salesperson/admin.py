from django.contrib import admin

from .models import Salesperson

@admin.register(Salesperson)
class SalespersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number')  # Customize the displayed columns
    search_fields = ('name', 'email', 'phone_number')  # Add search functionality
