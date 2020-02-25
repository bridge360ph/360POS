from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.serializers.users import UserSerializer
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


class FuelViewSet(viewsets.ModelViewSet):
    queryset = FuelPricing.objects.all()
    serializer_class = FuelPricingSerializer
    permission_classes = [IsAuthenticated]


class GasStationViewSet(viewsets.ModelViewSet):
    queryset = GasStations.objects.all()
    serializer_class = GasolineSerializer
    permission_classes = [IsAuthenticated]