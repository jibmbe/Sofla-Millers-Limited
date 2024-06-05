from django.urls import path
from .views import create_transaction, generate_daily_stock_report, stock_list, stock_report

urlpatterns = [
    path('create-transaction/', create_transaction, name='create_transaction'),
    path('stock-report', stock_report, name='stock_report'),
    path('stocks/', stock_list, name='stock_list'),
     path('generate-daily-stock-report/', generate_daily_stock_report, name='generate_daily_stock_report'),
]
