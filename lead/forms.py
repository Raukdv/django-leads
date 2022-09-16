from django import forms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import (
    login, authenticate
)

from lead.models.leads import Leads
from lead.validators import FileUploadValidatorForm

import re
import phonenumbers

class LeadsForm(forms.ModelForm):
    client = forms.CharField(required=True, label='Client Name', 
    widget = forms.TextInput(attrs={
        'class':'form-control',
        'placeholder': 'client',
    }))

    address = forms.CharField(required=False, label='Address', help_text='Phone its a very sensitive field, please use the US format only', 
    widget = forms.TextInput(attrs={
        'class':'form-control', 
        'placeholder': 'address',
    }))

    city = forms.CharField(required=False, label='City',
    widget = forms.TextInput(attrs={
        'class':'form-control', 
        'placeholder': 'city',
    }))

    state = forms.CharField(required=False, label='State',
    widget = forms.TextInput(attrs={
        'class':'form-control', 
        'placeholder': 'state',
    }))

    zipcode = forms.CharField(required=False, label='Zip code',
    widget = forms.TextInput(attrs={
        'class':'form-control', 
        'placeholder': 'zipcode',
    }))

    phoneNumber = forms.CharField(required=False, label='Phone', help_text='Phone its a very sensitive field, please use the US format only', 
    widget = forms.TextInput(attrs={
        'class':'form-control', 
        'placeholder': 'phone',
        'type':'tel'
    }))

    category = forms.CharField(required=False, label='Category / Type',
    widget = forms.TextInput(attrs={
        'class':'form-control', 
        'placeholder': 'category',
    }))

    date = forms.CharField(required=False, label='Date',
    widget = forms.TextInput(attrs={
        'class':'form-control', 
        'placeholder': 'date',
    }))

    description = forms.CharField(required=False, label='description',
    widget = forms.Textarea(attrs={
        'class':'form-control', 
        'placeholder': 'description',
    }))

    price = forms.IntegerField(required=False, widget = forms.NumberInput(attrs={'class':'form-control',
        'id':'price',
        'placeholder': 'price',
    }))

    def clean(self):
        cleaned_data = super().clean()

        if not cleaned_data.get('phoneNumber'):
            raise forms.ValidationError(_("One phone is required."))
        
        try:
            my_number = phonenumbers.parse(cleaned_data['phoneNumber'], "US")
        except:
            raise forms.ValidationError(_("One phone is required."))

        if phonenumbers.is_possible_number(my_number) or phonenumbers.is_valid_number(my_number):
            my_number_formatted = phonenumbers.format_number(my_number, phonenumbers.PhoneNumberFormat.E164)
            cleaned_data['phone'] = str(my_number_formatted)
        else:
            raise forms.ValidationError(_("Phone is not a valid number for US."))

        return cleaned_data
    
    class Meta:
        fields = ['client', 'address', 'city', 'state', 'zipcode', 'phoneNumber', 'category', 'date', 'description', 'price']
        exclude = (
            'date_creation', 'taken',
        )
        model = Leads
        field_order = ['client', 'address', 'city', 'state', 'zipcode', 'phoneNumber', 'category', 'date', 'description', 'price']

class CustomerUploadForm(FileUploadValidatorForm, forms.ModelForm):
    form_class = LeadsForm

    def save(self, commit=True):
        object_list = list()
        for form in self.form_list:
            object_list.append(
                form.save(commit=commit)
                )
        return object_list

    class Meta:
        fields = ('file', )
        model = Leads
            