# Generated by Django 4.2.7 on 2024-06-01 12:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('suppliers', '0002_supplier_vehicle_number_plate'),
    ]

    operations = [
        migrations.CreateModel(
            name='QualityControlRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('aflatoxin_before_milling', models.FloatField()),
                ('aflatoxin_after_milling', models.FloatField()),
                ('moisture_content', models.FloatField()),
                ('number_of_bags', models.IntegerField()),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='suppliers.supplier')),
            ],
        ),
    ]
