import datetime

from django.db.models import Q

from rest_framework import serializers, viewsets
from rest_framework.fields import SerializerMethodField
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from gasolinestation.models import FuelPricing


class FuelPricingSerializer(serializers.ModelSerializer):

    class Meta:
        model = FuelPricing
        fields = "__all__"


class FuelViewSet(viewsets.ModelViewSet):
    queryset = FuelPricing.objects.all()
    serializer_class = FuelPricingSerializer
    permission_classes = [IsAuthenticated]