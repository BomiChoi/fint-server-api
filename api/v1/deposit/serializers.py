import hashlib

from django.db import transaction
from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from apps.account.models import Account, Deposit, AccountAsset
from apps.asset.models import Asset
from apps.user.models import User


class DepositValidateSerializer(serializers.ModelSerializer):
    account_number = serializers.CharField(max_length=30, write_only=True)
    user_name = serializers.CharField(max_length=30, write_only=True)
    transfer_amount = serializers.DecimalField(max_digits=16, decimal_places=2, write_only=True)

    def validate(self, attrs):
        """ 게좌번호로 계좌를 찾은 후 계정주와 사용자가 일치하는지 확인하고 반환합니다. """

        # 계좌 찾기
        account = get_object_or_404(Account, account_number=attrs.pop('account_number'))
        attrs['account'] = account

        # 사용자가 일치하는지 확인
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


class DepositRunSerializer(serializers.Serializer):
    signature = serializers.CharField(write_only=True)
    transfer_identifier = serializers.CharField(write_only=True)
    status = serializers.BooleanField(read_only=True)

    def validate(self, attrs):
        """ 암호화된 데이터가 저장된 입금내역과 일치하는지 확인하고 입금내역이 인증대기 상태가 맞는지 확인합니다. """

        # 저장된 입금내역과 일치하는지 확인
        deposit = get_object_or_404(Deposit, id=attrs['transfer_identifier'])
        s = deposit.account.account_number + deposit.account.user.name + str(int(deposit.transfer_amount))
        encoded = hashlib.sha256(s.encode()).hexdigest()
        if encoded != attrs['signature']:
            raise ValidationError({'transfer_identifier', '입력받은 정보가 저장된 입금내역과 일치하지 않습니다.'})

        # 인증대기 상태가 맞는지 확인
        if deposit.status != '인증대기':
            raise ValidationError({'transfer_identifier', '이미 인증된 입금내역입니다.'})

        return attrs

    @transaction.atomic()
    def create(self, validated_data):
        """ 입금내역 상태를 인증완료로 변경하고 자산을 업데이트합니다. """

        try:
            # 입금내역 상태 변경
            deposit = Deposit.objects.get(id=validated_data['transfer_identifier'])
            deposit.status = '인증완료'
            deposit.save()

            # 투자 원금 업데이트
            deposit.account.principal += deposit.transfer_amount
            deposit.account.save()

            # 현금 자산 업데이트
            cash = Asset.objects.get(isin='CASH')
            account_asset = AccountAsset.objects.get(account=deposit.account, asset=cash)
            account_asset.current_price += deposit.transfer_amount
            account_asset.save()

            return {'status': True}

        except:
            return {'status': False}
