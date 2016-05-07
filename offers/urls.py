from offers import views
from utils.routers import SharedAPIRootRouter
router = SharedAPIRootRouter()
from django.conf.urls import url, include

router.register(r'offer', views.OfferViewSet)
router.register(r'offerhistory', views.OfferHistoryViewSet)
router.register(r'offerreview', views.OfferReviewViewSet)
router.register(r'nearestoffer', views.NearestOffer)


# near_offer = views.NearestOffer.as_view({
#     'get': 'list',
# })


# urlpatterns = [
#     url(
#         regex=r'^nearestoffer',
#         view=near_offer,
#         name="near-offer"
#     ),
# ]
