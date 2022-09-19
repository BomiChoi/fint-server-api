from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import AssetReadOnlyViewSet

router = DefaultRouter()
router.register('', AssetReadOnlyViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
