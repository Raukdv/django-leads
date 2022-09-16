from django.db import models
from django.utils.translation import gettext_lazy as _

from django.db.models.signals import pre_save, post_save

class Billing(models.Model):
    number_billing = models.CharField(max_length=15, null=True, blank=True, verbose_name=_("Number billing"))

    created_at = models.DateField(auto_now_add=True, verbose_name=_("Created at"))

    person = models.ForeignKey('core.User', null=True, blank=True, on_delete=models.CASCADE, verbose_name=_("Person"))
    
    leads_purchased = models.ManyToManyField('lead.Leads', verbose_name=_("Leads purchased"))

    def __str__(self):
        return self.person

def billing_number(sender, instance, *args, **kargs):
    import datetime
    import random
    import string

    x = datetime.datetime.now()

    code = ''.join(random.choice(string.digits) for x in range(4))
    instance.number_billing = x.strftime("%y")+x.strftime("%m")+x.strftime("%d")+code

#Signals
pre_save.connect(billing_number, sender=Billing)