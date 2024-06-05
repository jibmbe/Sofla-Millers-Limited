from django.db import models
from purchases.models import Purchase
from inventory.models import InventoryItem
from price_catalogue.models import PriceCatalogue
from production.models import ProductionRecord
from customers.models import Customer
from sales.models import Sale
from payroll.models import Employee
from finance.models import Expense
from reports.models import Report
from suppliers.models import Supplier  # Assuming you have a suppliers model
from stock.models import StockItem  # Assuming you have a stock items model
from quality_control.models import QualityControlRecord  # Assuming you have a quality control model

class DashboardMetrics(models.Model):
    total_purchases = models.IntegerField(default=0)
    total_inventory_items = models.IntegerField(default=0)
    total_price_catalogue_items = models.IntegerField(default=0)
    total_production_records = models.IntegerField(default=0)
    total_customers = models.IntegerField(default=0)
    total_sales = models.IntegerField(default=0)
    total_employees = models.IntegerField(default=0)
    total_expenses = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    total_reports = models.IntegerField(default=0)
    total_suppliers = models.IntegerField(default=0)
    total_stock_items = models.IntegerField(default=0)
    avg_aflatoxin_before = models.FloatField(default=0.0)
    avg_aflatoxin_after = models.FloatField(default=0.0)
    avg_moisture_content = models.FloatField(default=0.0)

    class Meta:
        verbose_name = "Dashboard Metrics"
        verbose_name_plural = "Dashboard Metrics"

    @classmethod
    def update_metrics(cls):
        cls.objects.all().delete()  # Clear existing data
        metrics = cls()
        metrics.total_purchases = Purchase.objects.count()
        metrics.total_inventory_items = InventoryItem.objects.count()
        metrics.total_price_catalogue_items = PriceCatalogue.objects.count()
        metrics.total_production_records = ProductionRecord.objects.count()
        metrics.total_customers = Customer.objects.count()
        metrics.total_sales = Sale.objects.count()
        metrics.total_employees = Employee.objects.count()
        metrics.total_expenses = Expense.objects.aggregate(models.Sum('amount'))['amount__sum'] or 0.00
        metrics.total_reports = Report.objects.count()
        metrics.total_suppliers = Supplier.objects.count()
        metrics.total_stock_items = StockItem.objects.count()

        # Calculating quality control averages
        quality_records = QualityControlRecord.objects.all()
        if quality_records.exists():
            metrics.avg_aflatoxin_before = quality_records.aggregate(models.Avg('aflatoxin_before'))['aflatoxin_before__avg'] or 0.0
            metrics.avg_aflatoxin_after = quality_records.aggregate(models.Avg('aflatoxin_after'))['aflatoxin_after__avg'] or 0.0
            metrics.avg_moisture_content = quality_records.aggregate(models.Avg('moisture_content'))['moisture_content__avg'] or 0.0

        metrics.save()
