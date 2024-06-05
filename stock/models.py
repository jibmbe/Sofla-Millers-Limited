from django.db import models
from django.utils import timezone

class Product(models.Model):
    name = models.CharField(max_length=100)
    unit = models.CharField(max_length=10)  # e.g., "kg", "units"

    def __str__(self):
        return self.name

class Stock(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    opening_stock = models.IntegerField(default=0)
    closing_stock = models.IntegerField(default=0)
    available_stock = models.IntegerField(default=0)
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.product.name} - {self.date}"

class Transaction(models.Model):
    TRANSACTION_TYPE_CHOICES = [
        ('sale', 'Sale'),
        ('purchase', 'Purchase')
    ]

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPE_CHOICES)
    transaction_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.product.name} - {self.transaction_type} - {self.quantity}"
    



class StockItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.product.name} - {self.date}"
 
