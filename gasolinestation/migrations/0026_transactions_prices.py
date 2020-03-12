# Generated by Django 3.0.3 on 2020-03-11 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gasolinestation', '0025_fuelprices_fuel_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='transactions',
            name='prices',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=9, null=True),
        ),
    ]
