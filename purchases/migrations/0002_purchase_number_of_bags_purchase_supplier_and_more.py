# Generated by Django 4.2.7 on 2024-06-01 12:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('suppliers', '0002_supplier_vehicle_number_plate'),
        ('purchases', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='number_of_bags',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='purchase',
            name='supplier',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='suppliers.supplier'),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='item_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='quantity',
            field=models.IntegerField(),
        ),
    ]