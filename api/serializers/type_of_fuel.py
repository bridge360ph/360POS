from django.db.models import Q

from rest_framework import serializers, viewsets
from rest_framework.fields import SerializerMethodField
from rest_framework.permissions import IsAuthenticated

from gasolinestation.models import TypeOfFuel


class TypeOfFuelSerializer(serializers.ModelSerializer):

    class Meta:
        model = TypeOfFuel
        fields = "__all__"


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