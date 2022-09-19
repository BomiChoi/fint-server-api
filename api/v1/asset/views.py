from rest_framework.viewsets import ReadOnlyModelViewSet

from apps.asset.models import Asset
from .serializers import AssetSerializer


class AssetReadOnlyViewSet(ReadOnlyModelViewSet):
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer
