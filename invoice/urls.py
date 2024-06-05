from django.urls import path
from . import views

urlpatterns = [
    path('<str:invoice_number>/', views.invoice_detail, name='invoice_detail'),
]
