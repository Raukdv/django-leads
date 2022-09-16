from django import forms
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

import django_filters as filters

from lead import models

class MyLeadsFilterSet(filters.FilterSet):
    # client = filters.CharFilter(
    #     label=_("client"), lookup_expr='icontains'
    # )
    o = filters.OrderingFilter(
        fields=('client', ),
        widget=forms.HiddenInput
    )
    class Meta:
        model = models.Leads
        fields = {
            'client': ['icontains'],
            'zipcode': ['exact'],
            'category': ['icontains'],
            'city': ['icontains'],
            'state': ['icontains']
        }
        # fields = (
        #     'client', 'o'
        # )