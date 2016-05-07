# Create your views here.
from rest_framework import viewsets
from offers.models import Offer, OfferHistory, OfferReview
from offers.serializers import (
    OfferSerializer,
    OfferHistorySerializer,
    OfferReviewSerializer
)
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from math import radians, cos, sin, asin, sqrt


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

    # def get_queryset(self):
    #     queryset = Offer.objects.all()
    #     import pdb; pdb.set_trace()
    #     offer_id = self.request.query_params.get('offer',None)
    #     if offer_id:
    #         queryset.filter(offer__id=offer_id)
    #     return queryset


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
                offers.append(offer_data)

        return Response(
            offers,
            status=status.HTTP_200_OK)
