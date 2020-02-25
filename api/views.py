from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.serializers.users import UserSerializer
from users.models import CustomUser as user


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        users = user.objects.all()
        current_user = self.request.user.username
        
        if users:
            qs = users.filter(username=current_user)
            return qs