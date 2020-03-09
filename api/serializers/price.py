import datetime

from django.db.models import Q

from rest_framework import serializers, viewsets
from rest_framework.fields import SerializerMethodField
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from gasolinestation.models import PriceManagement, TypeOfFuel, GasolineStation


class PriceManagementSerializer(serializers.ModelSerializer):
    type_of_fuel = serializers.SlugRelatedField(slug_field="name", queryset=TypeOfFuel.objects.all(), allow_null=True, required=False)
    gas_station_assigned = serializers.SlugRelatedField(slug_field="name", queryset=GasolineStation.objects.all(), allow_null=True, required=False)

    class Meta:
        model = PriceManagement
        fields = '__all__'


class PriceManagementViewSet(viewsets.ModelViewSet):
    queryset = PriceManagement.objects.all()
    serializer_class = PriceManagementSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        cashier = self.request.user.position == 'Cashier'
        manager = self.request.user.position == 'Manager'
        owner = self.request.user.position == 'Owner'

        if cashier:
            return serializer.save(created_by=self.request.user.full_name)
        elif manager:
            return serializer.save(created_by=self.request.user.full_name)
        elif owner:
            return serializer.save(created_by=self.request.user.full_name)

    def perform_update(self, serializer):
        cashier = self.request.user.position == 'Cashier'
        manager = self.request.user.position == 'Manager'
        owner = self.request.user.position == 'Owner'

        if cashier:
            return serializer.save(updated_by=self.request.user.full_name)
        elif manager:
            return serializer.save(updated_by=self.request.user.full_name)
        elif owner:
            return serializer.save(updated_by=self.request.user.full_name)