from django.core.management.base import BaseCommand
from dashboard.models import DashboardMetrics

class Command(BaseCommand):
    help = 'Update dashboard metrics'

    def handle(self, *args, **kwargs):
        DashboardMetrics.update_metrics()
        self.stdout.write(self.style.SUCCESS('Successfully updated dashboard metrics'))