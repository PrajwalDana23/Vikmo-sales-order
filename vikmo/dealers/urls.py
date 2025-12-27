from rest_framework.routers import DefaultRouter
from .views import DealerViewSet

router = DefaultRouter()
router.register('', DealerViewSet)

urlpatterns = router.urls