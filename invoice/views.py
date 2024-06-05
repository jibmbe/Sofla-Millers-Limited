from django.shortcuts import render, get_object_or_404
from .models import Invoice

def invoice_detail(request, invoice_number):
    invoice = get_object_or_404(Invoice, invoice_number=invoice_number)
    return render(request, 'invoice/invoice_detail.html', {'invoice': invoice})