# Generated by Django 4.2.7 on 2024-05-18 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suppliers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='supplier',
            name='vehicle_number_plate',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
