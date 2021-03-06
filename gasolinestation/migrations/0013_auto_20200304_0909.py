# Generated by Django 3.0.3 on 2020-03-04 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gasolinestation', '0012_transactionsales'),
    ]

    operations = [
        migrations.AddField(
            model_name='transactionsales',
            name='dispensed_liter',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True),
        ),
        migrations.AlterField(
            model_name='transactionsales',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True),
        ),
    ]
