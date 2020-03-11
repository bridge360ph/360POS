from django.urls import include, path

from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

from api.serializers.fuels import FuelViewSet
from api.serializers.price import PriceManagementViewSet
from api.serializers.users import UserViewSet, ManagerViewSet, StaffViewSet
from api.serializers.gasoline import GasStationViewSet
from api.serializers.gasoline_stations import GasolineStationViewSet
from api.serializers.price import PriceManagementViewSet
from api.serializers.type_of_fuel import TypeOfFuelViewSet
from api.serializers.fuel_prices import FuelPriceViewSet
from api.serializers.transactions import TransactionViewSet


router = DefaultRouter()
router.register(r'user', UserViewSet, basename='users')
router.register(r'manager', ManagerViewSet, basename='managers')
router.register(r'staff', StaffViewSet, basename='staffs')
router.register(r'gas-station', GasStationViewSet, basename='gas')
router.register(r'gasoline-stations', GasolineStationViewSet)
router.register(r'fuel-pricing', FuelViewSet)
router.register(r'price-management', PriceManagementViewSet)
router.register(r'type-of-fuel', TypeOfFuelViewSet)
router.register(r'fuel-prices', FuelPriceViewSet)
router.register(r'transactions', TransactionViewSet, basename='transaction')


urlpatterns = [
    path('', include(router.urls)),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('api-token-auth/', views.obtain_auth_token)
]