# Generated by Django 4.2.7 on 2024-06-02 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_dashboardmetrics_avg_aflatoxin_after_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='dashboardmetrics',
            name='aflatoxin_test_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='dashboardmetrics',
            name='moisture_test_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
