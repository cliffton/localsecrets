from django.conf.urls import url, include
from accounts import views
from utils.routers import SharedAPIRootRouter
router = SharedAPIRootRouter()


router.register(r'user', views.UserViewSet)
router.register(r'customer', views.CustomerViewSet)
router.register(r'vendor', views.VendorViewSet)
router.register(r'register', views.UserRegisterView)

# user_registration = views.UserRegisterView.as_view({
#     'post': 'create',
# })

# urlpatterns = [
#     url(
#         regex=r'^user/register/$',
#         view=user_registration,
#         name="register"
#     ),
# ]
