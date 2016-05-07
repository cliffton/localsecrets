from offers import views
from utils.routers import SharedAPIRootRouter
router = SharedAPIRootRouter()


router.register(r'Offer', views.OfferViewSet)
router.register(r'OfferHistory', views.OfferHistoryViewSet)
router.register(r'OfferReview', views.OfferReviewViewSet)
