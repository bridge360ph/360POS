from datetime import datetime, timedelta

from django.db.models import Avg, Sum, Q
from . models import Transactions, FuelPrices

from django.shortcuts import render

from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'

    def get(self, request):
        one_week_ago = datetime.today() - timedelta(days=7)
        weekly_sales = Transactions.objects.filter(
            created_at__gte=one_week_ago).aggregate(Sum('sales'))
        weekly_liter = Transactions.objects.filter(
            created_at__gte=one_week_ago).aggregate(Sum('dispensed_liter'))
        weekly_price = Transactions.objects.filter(
            created_at__gte=one_week_ago).aggregate(Sum('prices'))
        
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
    model = Transactions
    template_name = 'sales/TransactionsTable.html'

    def get(self, request):
        today = datetime.today()
        one_week_ago = datetime.today() - timedelta(days=7)
        yearly = datetime.today().year
        sales = Transactions.objects.all().aggregate(Sum('sales'))
        today_sales = Transactions.objects.filter(
            created_at=today).aggregate(Sum('sales'))
        weekly_sales = Transactions.objects.filter(
            created_at__gte=one_week_ago).aggregate(Sum('sales'))
        yearly_sales = Transactions.objects.filter(
            created_at__year=yearly).aggregate(Sum('sales'))
        liter = Transactions.objects.all().aggregate(Sum('dispensed_liter'))
        today_liter = Transactions.objects.filter(
            created_at=today).aggregate(Sum('dispensed_liter'))
        weekly_liter = Transactions.objects.filter(
            created_at__gte=one_week_ago).aggregate(Sum('dispensed_liter'))
        yearly_liter = Transactions.objects.filter(
            created_at__year=yearly).aggregate(Sum('dispensed_liter'))
        price = Transactions.objects.all().aggregate(Sum('prices'))
        today_price = Transactions.objects.filter(
            created_at=today).aggregate(Sum('prices'))
        weekly_price = Transactions.objects.filter(
            created_at__gte=one_week_ago).aggregate(Sum('prices'))
        yearly_price = Transactions.objects.filter(
            created_at__year=yearly).aggregate(Sum('prices'))

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
