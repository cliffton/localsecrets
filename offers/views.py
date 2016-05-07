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
