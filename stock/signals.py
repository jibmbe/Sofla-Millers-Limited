# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Transaction, Stock

@receiver(post_save, sender=Transaction)
def update_stock_on_transaction(sender, instance, **kwargs):
    stock, created = Stock.objects.get_or_create(product=instance.product, date=instance.transaction_date.date())
    if created:
        stock.opening_stock = stock.available_stock
    
    if instance.transaction_type == 'sale':
        stock.available_stock -= instance.quantity
    elif instance.transaction_type == 'purchase':
        stock.available_stock += instance.quantity

    stock.closing_stock = stock.available_stock
    stock.save()
