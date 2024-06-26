# Generated by Django 4.2.7 on 2024-06-02 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dashboardmetrics',
            name='avg_aflatoxin_after',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='dashboardmetrics',
            name='avg_aflatoxin_before',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='dashboardmetrics',
            name='avg_moisture_content',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='dashboardmetrics',
            name='total_stock_items',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='dashboardmetrics',
            name='total_suppliers',
            field=models.IntegerField(default=0),
        ),
    ]
