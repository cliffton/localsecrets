from __future__ import unicode_literals

from django.db import models
from model_utils.models import TimeStampedModel
from django.contrib.auth.models import User
from shops.models import Shop
# Create your models here.


class Offer(TimeStampedModel):
    categories = {
        0: 'Tech',
        1: 'Food',
        2: 'Lifestyle'
    }

    shop = models.ForeignKey(Shop, related_name="offers")
    name = models.CharField(max_length=300)
    expiration = models.DateTimeField()
    count = models.IntegerField(default=0)
    description = models.TextField(null=True)
    category = models.IntegerField(default=0)
    tnc = models.TextField(null=True)

    def __str__(self):
        return self.name


class OfferHistory(TimeStampedModel):
    offer = models.ForeignKey(Offer, related_name="offer_history")
    user = models.ForeignKey(User, related_name="offers_used")

    def save(self, *args, **kwargs):
        if not self.pk:
            self.offer.count = self.offer.count + 1
            self.offer.save()
        super(OfferHistory, self).save(*args, **kwargs)

    def __str__(self):
        return "%s <-> %s" % (self.offer.name, self.user.get_full_name())


class OfferReview(TimeStampedModel):
    offer = models.ForeignKey(Offer, related_name="offer_reviews")
    user = models.ForeignKey(User, related_name="offers_reviewed")
    review = models.TextField()

    def __str__(self):
        return "%s <-> %s" % (self.offer.name, self.user.get_full_name())
