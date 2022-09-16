from typing_extensions import Required
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

    email = models.EmailField(verbose_name=_("Email"), unique=True)

    first_name = models.CharField(max_length=45, verbose_name=_("First name"))

    last_name = models.CharField(max_length=80, verbose_name=_("Last name"))

    phoneNumber = models.TextField(verbose_name=_("Phone number"), null=True, blank=True)

    address = models.CharField(max_length=100, verbose_name=_("Address"))

    my_leads = models.ManyToManyField('lead.Leads', blank=True, verbose_name=_("My Leads"))

    my_credits = models.IntegerField(default=0, verbose_name=_("Credits"))