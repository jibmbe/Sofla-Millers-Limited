from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Product, Stock, StockItem, Transaction
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
import logging

logger = logging.getLogger(__name__)

def create_transaction(request):
    if request.method == "POST":
        product_id = request.POST.get('product_id')
        quantity = int(request.POST.get('quantity'))
        transaction_type = request.POST.get('transaction_type')

        product = get_object_or_404(Product, id=product_id)

        # Create transaction
        transaction = Transaction.objects.create(
            product=product,
            quantity=quantity,
            transaction_type=transaction_type
        )

        # Update stock levels
        stock_item, created = StockItem.objects.get_or_create(product=product, date=timezone.now().date())
        if transaction_type == 'sale':
            stock_item.quantity -= quantity
        elif transaction_type == 'purchase':
            stock_item.quantity += quantity

        stock_item.save()

        return redirect('stock_report')

    products = Product.objects.all()
    return render(request, 'create_transaction.html', {'products': products})

def stock_list(request):
    stocks = Stock.objects.all()  # Query all stock items from the database
    return render(request, 'stock_list.html', {'stocks': stocks})

def stock_report(request):
    stocks = Stock.objects.filter(date=timezone.now().date())
    return render(request, 'stock_report.html', {'stocks': stocks})

def generate_daily_stock_report(request):
    # Query all stock items for the day
    stocks = Stock.objects.filter(date=timezone.now().date())

    # Log the number of stock items retrieved
    logger.info(f"Retrieved {stocks.count()} stock items")

    template_path = 'stock_report_template.html'
    context = {'stocks': stocks}

    # Render the template HTML
    template = get_template(template_path)
    html = template.render(context)

    # Log the rendered HTML
    logger.debug("Rendered HTML:")
    logger.debug(html)

    # Create a PDF response
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="daily_stock_report.pdf"'

    # Generate PDF from HTML
    pisa_status = pisa.CreatePDF(html, dest=response)

    # Check if PDF generation was successful
    if pisa_status.err:
        logger.error("Error generating PDF")
        return HttpResponse('Error generating PDF')

    return response
