import uuid

from decimal import Decimal

from django.db import models
from django.conf import settings


class ImportantInfo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    created_by = models.CharField(max_length=150, null=True, blank=True)
    updated_by = models.CharField(max_length=150, null=True, blank=True)


class GasolineStation(ImportantInfo):
    name = models.CharField(max_length=250, null=True, blank=True)

    class Meta:
        ordering = ['-name']

    def __str__(self):
        return "%s" % (self.name)


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

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return "%s" % (self.name)


class PriceManagement(ImportantInfo):
    type_of_fuel = models.ForeignKey(TypeOfFuel, null=True, blank=True, on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True, default=0.00)
    gas_station_assigned = models.ForeignKey(GasolineStation, null=True, blank=True, on_delete=models.PROTECT)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return "%s - %s" % (self.type_of_fuel, self.price)


class FuelPrices(ImportantInfo):
    name = models.CharField(max_length=150, null=True, blank=True)
    price = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True, default=0.00)
    gas_station_assigned = models.ForeignKey(GasolineStation, null=True, blank=True, on_delete=models.PROTECT)
    fuel_price = models.CharField(max_length=150, null=True, blank=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return "%s - %s" % (self.name, self.price)

    def combine_fuel_price(self):
        get_fuel_price = self.name + ' - ' + str(self.price)
        return get_fuel_price

    def save(self, *args, **kwargs):
        self.fuel_price = self.combine_fuel_price()
        super().save(*args, **kwargs)


class Transactions(ImportantInfo):
    fuel = models.ForeignKey(FuelPrices, null=True, blank=True, on_delete=models.PROTECT)
    gas_station_assigned = models.ForeignKey(GasolineStation, null=True, blank=True, on_delete=models.PROTECT)
    sales = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True, default=0.00)
    dispensed_liter = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True, default=0.00)
    
    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return "%s - %s" % (self.gas_station_assigned, self.dispensed_liter)
    
    def calculate_dispensed_liter(self):
        liter = Decimal(self.sales) / Decimal(self.fuel.price)
        total_liter = Decimal(liter)
        return total_liter
    
    def save(self, *args, **kwargs):
        self.dispensed_liter = self.calculate_dispensed_liter()
        super().save(*args, **kwargs)


class GasStations(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.ForeignKey(GasolineStation, null=True, blank=True, on_delete=models.PROTECT)
    site_location = models.CharField(max_length=150, null=True, blank=True)
    site_manager = models.ForeignKey(settings.AUTH_USER_MODEL,
        related_name='site_managers', null=True, blank=True, on_delete=models.PROTECT)
    site_staff = models.ManyToManyField(settings.AUTH_USER_MODEL,
        related_name='site_staffs', blank=True)
    fuel_prices = models.ManyToManyField(FuelPrices, blank=True)
    created_by = models.CharField(max_length=150, null=True, blank=True)
    updated_by = models.CharField(max_length=150, null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        ordering = ['-name']

    def __str__(self):
        return "%s"%(self.name)