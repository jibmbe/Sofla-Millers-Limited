from django.db import models

class Supplier(models.Model):
    name = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)
    address = models.TextField()
    vehicle_number_plate = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.name
