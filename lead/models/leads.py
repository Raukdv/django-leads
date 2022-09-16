from django.db import models
from django.utils import timezone

class Leads(models.Model):
    client = models.CharField(max_length=255, verbose_name=("Client"), null=False, blank=False)

    address = models.CharField(max_length=100, verbose_name=("Address"),null=False, blank=False)

    city = models.CharField(max_length=100, verbose_name=("City"),null=False, blank=False)

    state = models.CharField(max_length=100, verbose_name=("State"),null=False, blank=False)

    zipcode = models.CharField(max_length=25, verbose_name=("Zip Code"),null=False, blank=False)

    phoneNumber = models.CharField(max_length=50, verbose_name=("Phone number"),null=False, blank=False)

    category = models.CharField(max_length=100, verbose_name=("Category/Type"),null=False, blank=False)

    date =  models.CharField(max_length=25, verbose_name=("Date"), null=True, blank=True)

    date_creation = models.DateTimeField(default=timezone.now, verbose_name=("Date Creation"))

    description = models.TextField(verbose_name=("Description"),null=True, blank=True)

    price = models.PositiveIntegerField(verbose_name=("Price"), null=True, blank=True)
    
    taken = models.BooleanField(default=False, verbose_name=("Taken"), null=False, blank=False)

    
    def __str__(self):
        return self.client

    def get_date_object(self):
        from datetime import datetime
        date_object = datetime.strptime(self.date,"%m/%d/%Y %H:%M")
        return date_object

    def get_field_values(self):
        return [field.value_to_string(self) for field in Leads._meta.fields]