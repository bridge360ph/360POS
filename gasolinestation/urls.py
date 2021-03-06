from django.urls import path

from .views import HomeView,GasView, GasolineStationView, AddGasView, SalesView, PriceView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('gas-stations/', GasView.as_view(), name='gas'),
    path('gasoline-stations/', GasolineStationView.as_view(), name='gasoline-stations'),
    path('gas-stations/add', AddGasView.as_view(), name='gas-add'),
    path('sales/', SalesView.as_view(), name='sales'),
    path('price/', PriceView.as_view(), name='prices')
]