from django.db import models

from suppliers.models import Supplier


class QualityControlRecord(models.Model):
    date = models.DateField()
    aflatoxin_before_milling = models.FloatField()
    aflatoxin_after_milling = models.FloatField()
    moisture_content = models.FloatField()
    number_of_bags = models.IntegerField()  # Adding the number of bags field
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)

    def __str__(self):
        return f"QC Record for {self.date}"