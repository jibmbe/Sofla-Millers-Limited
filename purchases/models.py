from django.db import models
from suppliers.models import Supplier

class Purchase(models.Model):
    purchase_date = models.DateField()
    item_name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, default=1)
    number_of_bags = models.IntegerField(default=0)

    def __str__(self):
        return f"Purchase of {self.item_name} from {self.supplier} on {self.purchase_date}"
