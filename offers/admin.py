from django.contrib import admin
from offers.models import Offer, OfferHistory, OfferReview

admin.site.register(Offer)
admin.site.register(OfferHistory)
admin.site.register(OfferReview)
