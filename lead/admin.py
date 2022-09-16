from django.contrib import admin
from lead.models.leads import Leads
from lead.models.billing import Billing

# Register your models here.
@admin.register(Leads)
class LeadsAdmin(admin.ModelAdmin):

    list_display = ( 
         'client', 'zipcode', 'taken'
    )
    
    search_fields = (
        'client', 'zipcode', 'taken'
    )

    exclude = ('date_creation',)

@admin.register(Billing)
class BillingAdmin(admin.ModelAdmin):
    list_display = ( 
        'person', 'number_billing'
    )
    
    search_fields = (
        'person',
    )

    exclude = ('date_creation',)

