from __future__ import unicode_literals

from django.db import models
from model_utils.models import TimeStampedModel
from django.contrib.auth.models import User

# Create your models here.


class Customer(TimeStampedModel):
    user = models.ForeignKey(User, related_name="customer")
    contact_number = models.CharField(max_length=10, null=True)
    age = models.IntegerField(null=True)
    gender = models.CharField(null=True, max_length=20)

    def __str__(self):
        return self.user.get_full_name()


class Vendor(TimeStampedModel):
    user = models.ForeignKey(User, related_name="vendor")
    contact_number = models.CharField(max_length=10)
