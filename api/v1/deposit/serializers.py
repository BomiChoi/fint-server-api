from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from apps.account.models import Account, Deposit
from apps.user.models import User


class DepositValidateSerializer(serializers.ModelSerializer):
    account_number = serializers.CharField(max_length=30, write_only=True)
    user_name = serializers.CharField(max_length=30, write_only=True)
    transfer_amount = serializers.DecimalField(max_digits=16, decimal_places=2, write_only=True)

    def validate(self, attrs):
        account = get_object_or_404(Account, account_number=attrs.pop('account_number'))
        attrs['account'] = account
        user = get_object_or_404(User, name=attrs.pop('user_name'))
        if user != account.user:
            raise ValidationError({'user': '계정주와 사용자가 일치하지 않습니다.'})
        return attrs

    class Meta:
        model = Deposit
        fields = (
            'id',
            'account_number',
            'user_name',
            'transfer_amount'
        )
