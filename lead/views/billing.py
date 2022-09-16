#Redirects
from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

#Clases para las vistas
from django.views.generic import (
    CreateView, DeleteView, DetailView, 
    FormView, ListView, UpdateView, TemplateView, View
    )

#Tools
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from lead import filters

#Models
from lead.models.billing import Billing

#Mixins
from core.mixins import FilterMixin

class MyInvoiceListView(LoginRequiredMixin, ListView):
    model = Billing
    paginate_by = 10
    #filterset_class = filters.MyLeadsFilterSet
    template_name = 'billing_list.html'

    def get_queryset(self):
        queryset = Billing.objects.filter(person=self.request.user).order_by('-person')
        return queryset