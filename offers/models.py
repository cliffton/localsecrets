from __future__ import unicode_literals

from django.db import models
from model_utils.models import TimeStampedModel
from django.contrib.auth.models import User
from shops.models import Shop
from havenondemand.hodclient import *
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
        return "%s - %s" % (self.shop.name, self.name)


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
    sentiment = models.CharField(null=True, max_length=100, blank=True)
    score = models.FloatField(null=True, blank=True)

    def get_sentiment(self):
        # import pdb; pdb.set_trace()
        client = HODClient(
            '2f861e0d-c57b-4459-a9d9-5c87fa94fa15', version="v1")
        params = {
            'text': self.review
        }
        response = client.get_request(
            params, HODApps.ANALYZE_SENTIMENT, async=False)
        return response['aggregate']

    def save(self, *args, **kwargs):
        if self.pk:
            try:
                data = self.get_sentiment()
                self.sentiment = data['sentiment']
                self.score = data['score']
            except Exception, e:
                print e
                pass
        super(OfferReview, self).save(*args, **kwargs)

    def __str__(self):
        return "%s | %s | %s" % (self.offer.name, self.user.get_full_name(), self.id)
