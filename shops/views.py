# Create your views here.
from rest_framework import viewsets
from shops.models import Shop
from shops.serializers import ShopSerializer


class ShopViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
