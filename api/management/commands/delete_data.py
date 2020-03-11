from gasolinestation.models import GasStations, Transactions, GasolineStation, FuelPrices

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """
    Updates the Gas Station model's name to empty
    (this can be enhance along the way)
    """
    help = 'Update string to none for gas station'

    def handle(self, *args, **kwargs):
        Transactions.objects.all().delete()
        GasStations.objects.all().delete()
        FuelPrices.objects.all().delete()
        GasolineStation.objects.all().delete()
        self.stdout.write(self.style.SUCCESS("Fields are now empty"))
