from gasolinestation.models import GasStations, PriceManagement

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """
    Updates the Gas Station model's name to empty
    (this can be enhance along the way)
    """
    help = 'Update string to none for gas station'

    def handle(self, *args, **kwargs):
        GasStations.objects.all().update(name="")
        PriceManagement.objects.all().update(gas_station_assigned="")
        self.stdout.write(self.style.SUCCESS("Gas station's name is now empty"))
