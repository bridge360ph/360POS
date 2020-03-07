from django.db.models import Q

from rest_framework import serializers, viewsets
from rest_framework.fields import SerializerMethodField
from rest_framework.permissions import IsAuthenticated


from users.models import CustomUser as user
from gasolinestation.models import (
    GasStations, FuelPricing,
    )


class GasolineSerializer(serializers.ModelSerializer):
    site_manager = serializers.SlugRelatedField(slug_field="full_name", queryset=user.objects.filter(position="Manager"), allow_null=True, required=False)
    site_staff = serializers.SlugRelatedField(slug_field="full_name", queryset=user.objects.filter(position="Cashier"), allow_null=True, required=False, many=True)
    pricing_for_specific_type_of_fuel = serializers.SlugRelatedField(slug_field="name", queryset=FuelPricing.objects.all(), allow_null=True, required=False)

    class Meta:
        model = GasStations
        fields = "__all__"


class GasStationViewSet(viewsets.ModelViewSet):
    serializer_class = GasolineSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        employee_id = self.request.user.id
        if self.request.user.position == 'Cashier':

            gas = GasStations.objects.all()
            qs = gas.filter(Q(site_staff=employee_id))
            return qs
        if self.request.user.position == 'Manager':

            gas = GasStations.objects.all()
            qs = gas.filter(Q(site_manager=employee_id))
            return qs
        elif self.request.user.position == 'Owner':

            gas = GasStations.objects.all()
            return gas

    def perform_create(self, serializer):
        cashier = self.request.user.position == 'Cashier'
        manager = self.request.user.position == 'Manager'
        owner = self.request.user.position == 'Owner'

        if cashier:
            return serializer.save(created_by=self.request.user.full_name)
        elif manager:
            return serializer.save(site_manager=self.request.user, created_by=self.request.user.full_name)
        elif owner:
            return serializer.save()

    def perform_update(self, serializer):
        manager = self.request.user.position == 'Manager'
        owner = self.request.user.position == 'Owner'

        if manager:
            return serializer.save(updated_by=self.request.user.full_name)
        elif owner:
            return serializer.save(updated_by=self.request.user.full_name)