from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, View, ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from lead.models import Leads
from lead import filters

#Mixins
from core.mixins import FilterMixin

class IndexView(LoginRequiredMixin, FilterMixin, ListView):
    model = Leads
    template_name = 'panel/index.html'
    paginate_by = 20
    filterset_class = filters.MyLeadsFilterSet
    queryset = Leads.objects.all().order_by('?') #Use '?' will make de performance more slow.

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context