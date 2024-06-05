from django.urls import path
from . import views

urlpatterns = [
    path('', views.price_catalogue_list, name='price_catalogue_list'),
]
