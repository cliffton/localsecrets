"""localsecrets URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
# from accounts import urls as accounts_urls
from utils.routers import SharedAPIRootRouter
# from accounts import urls as accounts_urls

def api_urls():
    """
        Automatically discovers and imports all
        the api.urls from the registered apps.
        For Django REST Framework.
        http://stackoverflow.com/questions/20825029/registering-api-in-apps/22684199#22684199
    """
    from .settings import INSTALLED_APPS
    from importlib import import_module
    for app in INSTALLED_APPS:
        try:
            import_module(app + '.urls')
        except (ImportError, AttributeError):
            pass
    return SharedAPIRootRouter.shared_router.urls


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # url(r'^api/v1/user/register/', include(accounts_urls)),
    url(r'^api/v1/', include(api_urls())),
]


# urlpatterns += accounts_urls
