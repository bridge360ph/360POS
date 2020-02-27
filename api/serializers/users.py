from rest_framework import serializers
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