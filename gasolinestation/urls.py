from django.urls import path

from .views import HomeView,GasView, AddGasView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('gas-stations/', GasView.as_view(), name='gas'),
    path('gas-stations/add', AddGasView.as_view(), name='gas-add')
]