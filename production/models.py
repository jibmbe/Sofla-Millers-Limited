from django.db import models


class ProductionRecord(models.Model):
    product_name = models.CharField(max_length=255)
    quantity_produced = models.PositiveIntegerField()
    production_date = models.DateField()

    def __str__(self):
        return self.product_name
