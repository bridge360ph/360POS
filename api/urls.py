from django.urls import include, path

from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

from . views import (
    UserViewSet, GasStationViewSet, FuelViewSet,
    ManagerViewSet, StaffViewSet,
    )


router = DefaultRouter()
router.register(r'user', UserViewSet, basename='users')
router.register(r'manager', ManagerViewSet, basename='managers')
router.register(r'staff', StaffViewSet, basename='staffs')
router.register(r'gas-station', GasStationViewSet)
router.register(r'fuel-pricing', FuelViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('api-token-auth/', views.obtain_auth_token)
]