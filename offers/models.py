from __future__ import unicode_literals

from django.db import models
from model_utils.models import TimeStampedModel
from django.contrib.models import User
from shops.models import Shop
# Create your models here.


class Offer(TimeStampedModel):
    shop = models.ForeignKey(Shop, related_name="offers")
    name = models.CharField(max_length=300)
    expiration = models.DateTimeField()
    count = models.IntegerField(default=0)


class OfferHistory(TimeStampedModel):
    offer = models.ForeignKey(Offer, related_name="offer_history")
    user = models.ForeignKey(User, related_name="offers_used")

    def save(self, *args, **kwargs):
        if self.pk:
            self.offer.count = self.offer.count + 1
            self.offer.save()
        super(OfferHistory, self).save(*args, **kwargs)


class OfferReview(TimeStampedModel):
    offer = models.ForeignKey(Offer, related_name="offer_reviews")
    user = models.ForeignKey(User, related_name="offers_reviewed")
    review = models.TextField()
