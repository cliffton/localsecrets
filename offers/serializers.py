from rest_framework import serializers
from offers.models import Offer, OfferHistory, OfferReview


class OfferSerializer(serializers.ModelSerializer):
    expiration = serializers.DateTimeField(format="%d %b %Y %I %p")

    class Meta:
        model = Offer


class OfferHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = OfferHistory


class OfferReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = OfferReview
