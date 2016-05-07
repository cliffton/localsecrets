# Create your views here.
from rest_framework import viewsets
from offers.models import Offer, OfferHistory, OfferReview
from offers.serializers import (
    OfferSerializer,
    OfferHistorySerializer,
    OfferReviewSerializer
)


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
