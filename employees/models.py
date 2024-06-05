from django.db import models



class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    date_hired = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
