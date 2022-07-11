from .views import StoreAPI, MyStores
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('stores', StoreAPI)
router.register('my_stores', MyStores)
urlpatterns = router.urls
