from django.urls import path
from . import views

urlpatterns = [
    path('', views.sale_list, name='sale_list'),
]
