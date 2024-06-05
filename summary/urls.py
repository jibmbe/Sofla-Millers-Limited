from django.urls import path
from .views import daily_summary

urlpatterns = [
    path('daily-summary/', daily_summary, name='daily_summary'),
]