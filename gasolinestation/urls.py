from django.urls import path

from .views import HomeView,GasView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('gas-stations/', GasView.as_view(), name='gas')
]