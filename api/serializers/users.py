from rest_framework import serializers, viewsets
from rest_framework.fields import SerializerMethodField
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from users.models import CustomUser


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = (
            'id','username', 'first_name', 'last_name', 'nickname',
            'picture', 'position', 'birthdate', 'full_name'
        )


class ManagerSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = (
            "full_name",
        )


class StaffSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = (
            "full_name",
        )


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        users = CustomUser.objects.all()
        current_user = self.request.user.username

        if users:
            qs = users.filter(username=current_user)
            return qs


class ManagerViewSet(viewsets.ModelViewSet):
    serializer_class = ManagerSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        users = CustomUser.objects.all()

        if users:
            qs = users.filter(position="Manager")
            return qs


class StaffViewSet(viewsets.ModelViewSet):
    serializer_class = StaffSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        users = CustomUser.objects.all()

        if users:
            qs = users.filter(position="Cashier")
            return qs