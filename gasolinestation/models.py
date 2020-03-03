import uuid

from django.db import models
from django.conf import settings


class ImportantInfo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    created_by = models.CharField(max_length=150, null=True, blank=True)
    updated_by = models.CharField(max_length=150, null=True, blank=True)


class FuelPricing(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=150, null=True, blank=True)
    price = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True)
    currency = models.CharField(max_length=150, null=True, blank=True)

    class Meta:
        ordering = ['-name']

    def __str__(self):
        return '%s - %s %s'%(self.name, self.currency, self.price)


class TypeOfFuel(ImportantInfo):
    name = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        return "%s" % (self.name)


class GasStations(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=150, null=True, blank=True)
    site_location = models.CharField(max_length=150, null=True, blank=True)
    site_manager = models.ForeignKey(settings.AUTH_USER_MODEL,
        related_name='site_managers', null=True, blank=True, on_delete=models.PROTECT)
    site_staff = models.ManyToManyField(settings.AUTH_USER_MODEL,
        related_name='site_staffs', blank=True)
    pricing_for_specific_type_of_fuel = models.ForeignKey(FuelPricing, null=True, blank=True, on_delete=models.PROTECT)
    price_management_flexibility = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True)
    sales = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True)
    volume_of_gasoline = models.CharField(max_length=150, null=True, blank=True)
    created_by = models.CharField(max_length=150, null=True, blank=True)
    updated_by = models.CharField(max_length=150, null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        ordering = ['-name']

    def __str__(self):
        return "%s"%(self.name)


class PriceManagement(ImportantInfo):
    type_of_fuel = models.ForeignKey(TypeOfFuel, null=True, blank=True, on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True, default=0.00)
    gas_station_assigned = models.ForeignKey(GasStations, null=True, blank=True, on_delete=models.PROTECT)

    def __str__(self):
        return "%s - %s" % (self.type_of_fuel, self.price)


class TransactionSales(models.Model):
    type_of_fuel = models.ForeignKey(TypeOfFuel, null=True, blank=True, on_delete=models.PROTECT)
    sales = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True)
    price = models.ForeignKey(PriceManagement, null=True, blank=True, on_delete=models.PROTECT)
    gas_station_assigned = models.ForeignKey(GasStations, null=True, blank=True, on_delete=models.PROTECT)

    def __str__(self):
        return "Transaction sales for "+ ' ' +"%s" % (self.gas_station_assigned)