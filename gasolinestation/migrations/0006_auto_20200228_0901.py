# Generated by Django 3.0.3 on 2020-02-28 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gasolinestation', '0005_auto_20200228_0841'),
    ]

    operations = [
        migrations.AddField(
            model_name='gasstations',
            name='created_by_staff',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='gasstations',
            name='updated_by_manager',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
