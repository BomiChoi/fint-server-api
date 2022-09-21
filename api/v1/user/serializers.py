from rest_framework import serializers

from apps.account.models import Account
from apps.user.models import User


class UserAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = (
            'id',
            'stock_firm',
            'account_number',
            'account_name',
            'total_assets',
        )


class UserSerializer(serializers.ModelSerializer):
    account_set = UserAccountSerializer(many=True)

    class Meta:
        model = User
        fields = (
            'id',
            'name',
            'username',
            'account_set'
        )
