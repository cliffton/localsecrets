from shops import views
from utils.routers import SharedAPIRootRouter
router = SharedAPIRootRouter()


router.register(r'shop', views.ShopViewSet)
