import datetime

from django.db.models import Avg, Sum, Q
from . models import TransactionSales

from django.shortcuts import render

from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'


class GasView(LoginRequiredMixin, TemplateView):
    template_name = 'gas/GasTable.html'


class AddGasView(LoginRequiredMixin, TemplateView):
    template_name = 'gas/GasAdd.html'


class SalesView(LoginRequiredMixin, TemplateView):
    model = TransactionSales
    template_name = 'sales/SalesTable.html'

    def get(self, request):
        today = datetime.date.today()
        sales = TransactionSales.objects.all().aggregate(Sum('sales'))
        today_sales = TransactionSales.objects.filter(created_at=today).aggregate(Sum('sales'))
        liter = TransactionSales.objects.all().aggregate(Sum('dispensed_liter'))
        today_liter = TransactionSales.objects.filter(created_at=today).aggregate(Sum('dispensed_liter'))
        price = TransactionSales.objects.all().aggregate(Sum('price'))
        today_price = TransactionSales.objects.filter(created_at=today).aggregate(Sum('price'))
        ctx = {
            'sales': sales,
            'liter': liter,
            'price': price,
            'today_sales': today_sales,
            'today_liter': today_liter,
            'today_price': today_price
        }
        return render(request, self.template_name, ctx)

class PriceView(LoginRequiredMixin, TemplateView):
    template_name = 'price/PriceTable.html'


class FuelView(LoginRequiredMixin, TemplateView):
    template_name = 'fuel/FuelTable.html'