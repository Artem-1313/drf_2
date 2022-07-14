from .views import StoreAPI, MyStores, AdminStores
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('stores', StoreAPI)
router.register('my_stores', MyStores, basename="my_stores")
router.register('admin_stores', AdminStores, basename="admin_stores")
urlpatterns = router.urls
