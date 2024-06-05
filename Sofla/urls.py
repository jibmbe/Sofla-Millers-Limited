"""
URL configuration for Sofla project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from stock.views import create_transaction, stock_list, stock_report
from summary.views import daily_summary

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', include('dashboard.urls')), 
    path('suppliers/', include('suppliers.urls')),
    path('purchases/', include('purchases.urls')),
    path('inventory/', include('inventory.urls')),
    path('invoice/', include('invoice.urls')),
    path('price_catalogue/', include('price_catalogue.urls')),
    path('production/', include('production.urls')),
    path('customers/', include('customers.urls')),
    path('sales/', include('sales.urls')),
    path('payroll/', include('payroll.urls')),
    path('finance/', include('finance.urls')),
    path('reports/', include('reports.urls')),
    path('', include('website.urls')),
    path('stock/', include('stock.urls')),
    path('stocks/', stock_list, name='stock_list'),
    path('create-transaction/', create_transaction, name='create_transaction'),
    path('stock-report/', stock_report, name='stock_report'),
    path('daily-summary/', daily_summary, name='daily_summary'),
    
]
