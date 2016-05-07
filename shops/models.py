from __future__ import unicode_literals

from django.db import models
from model_utils.models import TimeStampedModel
from django.contrib.auth.models import User
# Create your models here.


class Shop(TimeStampedModel):
    user = models.ForeignKey(User, related_name="shops")
    name = models.CharField(max_length=300)
    latitude = models.DecimalField(max_digits=12, decimal_places=8, null=True)
    longitude = models.DecimalField(max_digits=12, decimal_places=8, null=True)

    def __str__(self):
        return self.name
