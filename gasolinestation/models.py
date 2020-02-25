import uuid

from django.db import models
from django.conf import settings


class FuelPricing(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=150, null=True, blank=True)
    price = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True)
    currency = models.CharField(max_length=150, null=True, blank=True)

    class Meta:
        ordering = ['-name']

    def __str__(self):
        return '%s - %s %s'%(self.name, self.currency, self.price)


class GasStations(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=150, null=True, blank=True)
    site_location = models.CharField(max_length=150, null=True, blank=True)
    site_manager = models.ForeignKey(settings.AUTH_USER_MODEL,
        related_name='site_managers', null=True, blank=True, on_delete=models.PROTECT)
    site_staff = models.ForeignKey(settings.AUTH_USER_MODEL,
        related_name='site_staffs', null=True, blank=True, on_delete=models.PROTECT)
    pricing_for_specific_type_of_fuel = models.ForeignKey(FuelPricing, null=True, blank=True, on_delete=models.PROTECT)
    price_management_flexibility = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        ordering = ['-name']

    def __str__(self):
        return "%s"%(self.name)