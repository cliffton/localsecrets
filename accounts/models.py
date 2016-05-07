from __future__ import unicode_literals

from django.db import models
from model_utils.models import TimeStampedModel
from django.contrib.models import User

# Create your models here.


class Customer(TimeStampedModel):
    user = models.ForeignKey(User, related_name="customer")
    contact_number = models.CharField(max_length=10)


class Vendor(TimeStampedModel):
    user = models.ForeignKey(User, related_name="vendor")
    contact_number = models.CharField(max_length=10)
