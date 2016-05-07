from accounts import views
from utils.routers import SharedAPIRootRouter
router = SharedAPIRootRouter()


router.register(r'user', views.UserViewSet)
router.register(r'customer', views.CustomerViewSet)
router.register(r'vendor', views.VendorViewSet)
