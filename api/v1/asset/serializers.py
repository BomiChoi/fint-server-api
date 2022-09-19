from rest_framework import serializers

from apps.asset.models import Asset


class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = (
            'id',
            'asset_name',
            'isin',
            'asset_group'
        )
