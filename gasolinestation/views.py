from datetime import datetime, timedelta

from django.db.models import Avg, Sum, Q
from . models import TransactionSales

from django.shortcuts import render

from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'

    def get(self, request):
        weekly_sales = TransactionSales.objects.filter(
            created_at__week=52).aggregate(Sum('sales'))
        weekly_liter = TransactionSales.objects.filter(
            created_at__week=52).aggregate(Sum('dispensed_liter'))
        weekly_price = TransactionSales.objects.filter(
            created_at__week=52).aggregate(Sum('price'))
        
        ctx = {
            'weekly_sales': weekly_sales,
            'weekly_liter': weekly_liter,
            'weekly_price': weekly_price
        }
        return render(request, self.template_name, ctx)


class GasView(LoginRequiredMixin, TemplateView):
    template_name = 'gas/GasTable.html'


class GasolineStationView(LoginRequiredMixin, TemplateView):
    template_name = 'gasoline_stations/GasTable.html'


class AddGasView(LoginRequiredMixin, TemplateView):
    template_name = 'gas/GasAdd.html'


class SalesView(LoginRequiredMixin, TemplateView):
    model = TransactionSales
    template_name = 'sales/TransactionsTable.html'

    def get(self, request):
        today = datetime.today()
        yearly = datetime.today().year
        sales = TransactionSales.objects.all().aggregate(Sum('sales'))
        today_sales = TransactionSales.objects.filter(
            created_at=today).aggregate(Sum('sales'))
        weekly_sales = TransactionSales.objects.filter(
            created_at__week=52).aggregate(Sum('sales'))
        yearly_sales = TransactionSales.objects.filter(
            created_at__year=yearly).aggregate(Sum('sales'))
        liter = TransactionSales.objects.all().aggregate(Sum('dispensed_liter'))
        today_liter = TransactionSales.objects.filter(
            created_at=today).aggregate(Sum('dispensed_liter'))
        weekly_liter = TransactionSales.objects.filter(
            created_at__week=52).aggregate(Sum('dispensed_liter'))
        yearly_liter = TransactionSales.objects.filter(
            created_at__year=yearly).aggregate(Sum('dispensed_liter'))
        price = TransactionSales.objects.all().aggregate(Sum('price'))
        today_price = TransactionSales.objects.filter(
            created_at=today).aggregate(Sum('price'))
        weekly_price = TransactionSales.objects.filter(
            created_at__week=52).aggregate(Sum('price'))
        yearly_price = TransactionSales.objects.filter(
            created_at__year=yearly).aggregate(Sum('price'))

        ctx = {
            'sales': sales,
            'liter': liter,
            'price': price,
            'today_sales': today_sales,
            'today_liter': today_liter,
            'today_price': today_price,
            'weekly_sales': weekly_sales,
            'weekly_liter': weekly_liter,
            'weekly_price': weekly_price,
            'yearly_sales': yearly_sales,
            'yearly_liter': yearly_liter,
            'yearly_price': yearly_price

        }
        return render(request, self.template_name, ctx)


class PriceView(LoginRequiredMixin, TemplateView):
    template_name = 'price/PriceTable.html'


class FuelView(LoginRequiredMixin, TemplateView):
    template_name = 'fuel/FuelTable.html'
