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
import random
from lead import filters

#Forms
from lead.forms import CustomerUploadForm 

#Models 
from lead.models.leads import Leads
from lead.models.billing import Billing
from core.models import User

#Mixins
from core.mixins import FilterMixin

class LeadsUploader(LoginRequiredMixin, FormView):
    template_name = 'uploaderform.html'
    form_class = CustomerUploadForm

    def get_form_class(self):
        return CustomerUploadForm

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy(
        'panel:lead:lead_my_list'
    )

class MyLeadsListView(LoginRequiredMixin, FilterMixin, ListView):
    model = Leads
    paginate_by = 20
    filterset_class = filters.MyLeadsFilterSet
    template_name = 'leads_list.html'

    def get_queryset(self):
        queryset = self.request.user.my_leads.all().order_by('-client')
        return queryset

class LeadsUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'lead_update.html'
    model = Leads
    
    fields = ['client','address','city','state','zipcode','phoneNumber','category','date','description','price']

class LeadsDetailView(LoginRequiredMixin, DetailView):
    template_name = 'lead_detail.html'
    model = Leads

class BuyLeads(LoginRequiredMixin, View):
    
    def get(self, request, *args, **kwargs):
        lead_selected = Leads.objects.get(id = kwargs['pk'])
        user_credits = request.user.my_credits

        if user_credits >= lead_selected.price:
            #if true, discount credits, add new lead and update it to taken
            request.user.my_credits = user_credits - lead_selected.price
            request.user.my_leads.add(lead_selected)
            request.user.save()
            lead_selected.taken = True
            lead_selected.save()
            #Billing information
            billing = Billing(person=request.user)
            billing.save()
            billing.leads_purchased.add(lead_selected)

            messages.success(request, "You've purchase one lead")
        else:
            messages.error(request, "Something was wrong")

        return HttpResponseRedirect(reverse_lazy('panel:index'))