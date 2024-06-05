from django.shortcuts import render
from django.db.models import Sum, Avg
from datetime import date, datetime
from purchases.models import Purchase
from sales.models import Sale
from production.models import ProductionRecord
from customers.models import Customer
from suppliers.models import Supplier
from stock.models import StockItem
from quality_control.models import QualityControlRecord



def daily_summary(request):
    date_str = request.GET.get('date')
    if date_str:
        try:
            summary_date = datetime.strptime(date_str, '%Y-%m-%d').date()
        except ValueError:
            summary_date = datetime.today().date()
    else:
        summary_date = datetime.today().date()

    # Summarizing purchases for the given date
    purchases = Purchase.objects.filter(purchase_date=summary_date)
    total_purchases = purchases.aggregate(Sum('quantity'))['quantity__sum'] or 0
    
    suppliers_today = purchases.values_list('supplier__name', flat=True).distinct()

    # Summarizing sales for the given date
    total_sales = Sale.objects.filter(sale_date=summary_date).aggregate(Sum('quantity_sold'))['quantity_sold__sum'] or 0

    # Summarizing production records for the given date
    total_production_records = ProductionRecord.objects.filter(production_date=summary_date).count()

    # Summarizing quality control data for the given date
    quality_records = QualityControlRecord.objects.filter(date=summary_date)
    avg_aflatoxin_before = quality_records.aggregate(Avg('aflatoxin_before_milling'))['aflatoxin_before_milling__avg'] or 0
    avg_aflatoxin_after = quality_records.aggregate(Avg('aflatoxin_after_milling'))['aflatoxin_after_milling__avg'] or 0
    avg_moisture_content = quality_records.aggregate(Avg('moisture_content'))['moisture_content__avg'] or 0
    total_bags = quality_records.aggregate(Sum('number_of_bags'))['number_of_bags__sum'] or 0

    # Counting customers
    total_customers = Customer.objects.count()

    # Counting suppliers
    total_suppliers = Supplier.objects.count()

    # Counting stock items
    total_stock_items = StockItem.objects.count()

    context = {
        'today': summary_date,
        'total_purchases': total_purchases,
        'total_sales': total_sales,
        'total_production_records': total_production_records,
        'total_customers': total_customers,
        'total_suppliers': total_suppliers,
        'total_stock_items': total_stock_items,
        'total_bags': total_bags,
        'suppliers_today': suppliers_today,
        'avg_aflatoxin_before': avg_aflatoxin_before,
        'avg_aflatoxin_after': avg_aflatoxin_after,
        'avg_moisture_content': avg_moisture_content,
    }

    return render(request, 'summary/daily_summary.html', context)
