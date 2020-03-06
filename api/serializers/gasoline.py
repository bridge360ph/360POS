from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from users.models import CustomUser as user
from gasolinestation.models import (
    GasStations, FuelPricing, PriceManagement,
    TypeOfFuel, TransactionSales
    )


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


class PriceManagementSerializer(serializers.ModelSerializer):
    type_of_fuel = serializers.SlugRelatedField(slug_field="name", queryset=TypeOfFuel.objects.all(), allow_null=True, required=False)
    gas_station_assigned = serializers.SlugRelatedField(slug_field="name", queryset=GasStations.objects.all(), allow_null=True, required=False)

    class Meta:
        model = PriceManagement
        fields = '__all__'


class TransactionSalesSerializer(serializers.ModelSerializer):
    type_of_fuel = serializers.SlugRelatedField(slug_field="name", queryset=TypeOfFuel.objects.all(), allow_null=True, required=False)
    gas_station_assigned = serializers.SlugRelatedField(slug_field="name", queryset=GasStations.objects.all(), allow_null=True, required=False)
    fuel_price = SerializerMethodField()

    class Meta:
        model = TransactionSales
        fields = '__all__'

    def get_fuel_price(self, obj):
        return str(obj.type_of_fuel) + ' - ' + str(obj.price)
        

class TypeOfFuelSerializer(serializers.ModelSerializer):

    class Meta:
        model = TypeOfFuel
        fields = "__all__"
