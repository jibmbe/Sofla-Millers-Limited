from django.db import models

from customers.models import Customer


class Sale(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=255)
    quantity_sold = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    sale_date = models.DateField()

    def __str__(self):
        return f"{self.customer} - {self.item_name}"