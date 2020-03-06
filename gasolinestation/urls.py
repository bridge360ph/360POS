from django.urls import path

from .views import HomeView,GasView, AddGasView, SalesView, PriceView, FuelView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('gas-stations/', GasView.as_view(), name='gas'),
    path('gas-stations/add', AddGasView.as_view(), name='gas-add'),
    path('sales/', SalesView.as_view(), name='sales'),
    path('price/', PriceView.as_view(), name='prices'),
    path('fuel/', FuelView.as_view(), name='fuels'),
]