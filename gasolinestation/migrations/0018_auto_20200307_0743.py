# Generated by Django 3.0.3 on 2020-03-07 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gasolinestation', '0017_remove_gasstations_volume_of_gasoline'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gasstations',
            name='fuels',
        ),
        migrations.AddField(
            model_name='gasstations',
            name='fuels',
            field=models.ManyToManyField(blank=True, to='gasolinestation.TypeOfFuel'),
        ),
    ]
