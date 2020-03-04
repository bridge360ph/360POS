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
    template_name = 'sales/SalesTable.html'


class PriceView(LoginRequiredMixin, TemplateView):
    template_name = 'price/PriceTable.html'