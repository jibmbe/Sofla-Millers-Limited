from django.db import models
from customers.models import Customer
from salesperson.models import Salesperson  # Ensure correct import

class Batch(models.Model):
    batch_number = models.CharField(max_length=20, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.batch_number

class Invoice(models.Model):
    invoice_number = models.CharField(max_length=20, unique=True)
    issue_date = models.DateField()
    due_date = models.DateField()
    sale = models.CharField(max_length=100)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    salesperson = models.ForeignKey(Salesperson, on_delete=models.CASCADE, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    batch = models.ForeignKey(Batch, on_delete=models.SET_NULL, null=True)  # Add this line

    def __str__(self):
        return self.invoice_number