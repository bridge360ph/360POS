from django.db.models import Q

from rest_framework import serializers, viewsets
from rest_framework.fields import SerializerMethodField
from rest_framework.permissions import IsAuthenticated


from users.models import CustomUser as user
from gasolinestation.models import GasolineStation


class GasolineStationSerializer(serializers.ModelSerializer):

    class Meta:
        model = GasolineStation
        fields = "__all__"


class GasolineStationViewSet(viewsets.ModelViewSet):
    queryset = GasolineStation.objects.all()
    serializer_class = GasolineStationSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        manager = self.request.user.position == 'Manager'
        owner = self.request.user.position == 'Owner'
        
        if manager:
            return serializer.save(site_manager=self.request.user, created_by=self.request.user.full_name)
        elif owner:
            return serializer.save(created_by=self.request.user.full_name)

    def perform_update(self, serializer):
        manager = self.request.user.position == 'Manager'
        owner = self.request.user.position == 'Owner'

        if manager:
            return serializer.save(updated_by=self.request.user.full_name)
        elif owner:
            return serializer.save(updated_by=self.request.user.full_name)