from django.db.models import Q

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.serializers.users import UserSerializer, ManagerSerializer, StaffSerializer
from api.serializers.gasoline import (
    GasolineSerializer, FuelPricingSerializer, PriceManagementSerializer,
    TransactionSalesSerializer, TypeOfFuelSerializer
    )

from users.models import CustomUser as user
from gasolinestation.models import (
    GasStations, FuelPricing, PriceManagement, TransactionSales, TypeOfFuel
    )


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
        employee_id = self.request.user.id
        gas = GasStations.objects.all()

        if gas:
            if self.request.user.position == 'Manager':

                qs = GasStations.objects.filter(Q(site_manager=employee_id))
                return qs
            elif self.request.user.position == 'Cashier':
                qs = GasStations.objects.filter(Q(site_staff=employee_id))
                return qs
                
            elif self.request.user.position == 'Owner':
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


class TransactionSalesViewSet(viewsets.ModelViewSet):
    queryset = TransactionSales.objects.all()
    serializer_class = TransactionSalesSerializer
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


class TypeOfFuelViewSet(viewsets.ModelViewSet):
    queryset = TypeOfFuel.objects.all()
    serializer_class = TypeOfFuelSerializer
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
        