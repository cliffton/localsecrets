from offers import views
from utils.routers import SharedAPIRootRouter
router = SharedAPIRootRouter()


router.register(r'offer', views.OfferViewSet)
router.register(r'offerhistory', views.OfferHistoryViewSet)
router.register(r'offerreview', views.OfferReviewViewSet)
