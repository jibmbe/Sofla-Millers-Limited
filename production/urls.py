from django.urls import path
from . import views

urlpatterns = [
    path('', views.production_list, name='production_list'),
]
