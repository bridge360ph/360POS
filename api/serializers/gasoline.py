from rest_framework import serializers

from users.models import CustomUser as user
from gasolinestation.models import GasStations, FuelPricing


class FuelPricingSerializer(serializers.ModelSerializer):

    class Meta:
        model = FuelPricing
        fields = "__all__"


class GasolineSerializer(serializers.ModelSerializer):
    site_manager = serializers.SlugRelatedField(slug_field="full_name", queryset=user.objects.filter(position="Manager"), allow_null=True, required=False)
    site_staff = serializers.SlugRelatedField(slug_field="full_name", queryset=user.objects.filter(position="Cashier"), allow_null=True, required=False, many=True)
    pricing_for_specific_type_of_fuel = serializers.SlugRelatedField(slug_field="name", queryset=FuelPricing.objects.all(), allow_null=True, required=False)

    class Meta:
        model = GasStations
        fields = "__all__"