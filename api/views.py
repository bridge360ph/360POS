from django.db.models import Q

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.serializers.users import UserSerializer, ManagerSerializer, StaffSerializer
from api.serializers.gasoline import GasolineSerializer, FuelPricingSerializer

from users.models import CustomUser as user
from gasolinestation.models import GasStations, FuelPricing


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        users = user.objects.all()
        current_user = self.request.user.username
        
        if users:
            qs = users.filter(username=current_user)
            return qs


class ManagerViewSet(viewsets.ModelViewSet):
    serializer_class = ManagerSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        users = user.objects.all()
        
        if users:
            qs = users.filter(position="Manager")
            return qs



class StaffViewSet(viewsets.ModelViewSet):
    serializer_class = StaffSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        users = user.objects.all()
        
        if users:
            qs = users.filter(position="Cashier")
            return qs


class FuelViewSet(viewsets.ModelViewSet):
    queryset = FuelPricing.objects.all()
    serializer_class = FuelPricingSerializer
    permission_classes = [IsAuthenticated]


class GasStationViewSet(viewsets.ModelViewSet):
    serializer_class = GasolineSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        employee_name = self.request.user.full_name
        owner = self.request.user.position == 'Owner'
        manager = self.request.user.position == 'Manager'
        cashier = self.request.user.position == 'Cashier'
        gas = GasStations.objects.all()

        if manager or cashier:
            qs = gas.filter(Q(site_manager__full_name=employee_name) |
                            Q(site_staff__full_name=employee_name))
            return qs
        elif owner:
            return gas

    def perform_create(self, serializer):
        employee_name = self.request.user.full_name
        manager = self.request.user.position == 'Manager'
        cashier = self.request.user.position == 'Cashier'

        if cashier:
            return serializer.save(created_by_staff=employee_name)
        elif manager:
            return serializer.save(updated_by_manager=employee_name)