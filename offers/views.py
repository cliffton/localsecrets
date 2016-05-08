# Create your views here.
from rest_framework import viewsets
from offers.models import Offer, OfferHistory, OfferReview
from offers.serializers import (
    OfferSerializer,
    OfferHistorySerializer,
    OfferReviewSerializer
)
from shops.serializers import ShopSerializer
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from math import radians, cos, sin, asin, sqrt
from accounts.models import User


def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    km = 6367 * c
    return km


class OfferViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer

    def get_queryset(self):
        queryset = Offer.objects.all()
        email = self.request.query_params.get('email', None)
        # user = User.objects.get(email=email)
        if email:
            queryset = queryset.filter(shop__user__email=email)
        return queryset


class OfferHistoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = OfferHistory.objects.all()
    serializer_class = OfferHistorySerializer


class OfferReviewViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = OfferReview.objects.all()
    serializer_class = OfferReviewSerializer

    def get_queryset(self):
        queryset = OfferReview.objects.all()
        offer_id = self.request.query_params.get('offer', None)
        if offer_id:
            queryset = queryset.filter(offer__id=offer_id)
        return queryset


class NearestOffer(viewsets.ViewSet):
    queryset = Offer.objects.all()
    # serializer_class = OfferSerializer

    def list(self, request):
        params = request.query_params
        offers = []
        if params:
            ulat = float(params['lat'])
            ulon = float(params['lon'])
            for offer in Offer.objects.select_related('shop').all():
                olat = float(offer.shop.latitude)
                olon = float(offer.shop.longitude)
                distance = haversine(ulat, ulon, olat, olon)
                offer_data = OfferSerializer(offer).data
                offer_data['distace'] = float(distance)
                offer_data['shop'] = ShopSerializer(offer.shop).data
                offers.append(offer_data)

        return Response(
            offers,
            status=status.HTTP_200_OK)


class OfferData(viewsets.ViewSet):
    queryset = Offer.objects.all()
    # serializer_class = OfferSerializer

    def retrieve(self, request, pk=None):
        if pk:
            offer = Offer.objects.get(pk=pk)
            total = offer.offer_reviews.all().count()
            positive = offer.offer_reviews.filter(sentiment="positive").count()
            negative = offer.offer_reviews.filter(sentiment="negative").count()
            neutral = offer.offer_reviews.filter(sentiment="neutral").count()
            response = {
                "positive": (float(positive) / total) * 100,
                "negative": (float(negative) / total) * 100,
                "neutral": (float(neutral) / total) * 100,
            }

        return Response(
            response,
            status=status.HTTP_200_OK)
