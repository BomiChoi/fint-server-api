from rest_framework import serializers

from apps.account.models import Account, AccountAsset


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = (
            'id',
            'account_name',
            'stock_firm',
            'account_number',
            'total_assets',
            'principal',
            'total_profits',
            'earnings_rate',
            'created_at',
            'updated_at',
        )


class AccountAssetSerializer(serializers.ModelSerializer):
    asset_name = serializers.CharField(read_only=True, source='asset.asset_name')

    class Meta:
        model = AccountAsset
        fields = (
            'id',
            'asset',
            'asset_name',
            'current_price',
            'count',
            'created_at',
            'updated_at',
            'evaluated_price',
        )
