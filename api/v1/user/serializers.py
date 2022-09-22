from django.contrib.auth.hashers import check_password
from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed

from apps.account.models import Account
from apps.user.authentication import generate_token
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


class LoginSerializer(serializers.Serializer):
    id = serializers.CharField(write_only=True, max_length=150)
    password = serializers.CharField(write_only=True, max_length=128, style={'input_type': 'password'})
    access_token = serializers.CharField(read_only=True)
    refresh_token = serializers.CharField(read_only=True)

    def validate(self, attrs):
        user = get_object_or_404(User, username=attrs['id'])
        if not check_password(attrs['password'], user.password):
            raise AuthenticationFailed({'password': '비밀번호가 틀립니다.'})
        attrs['user'] = user
        return attrs

    def create(self, validated_data):
        payload = {'username': validated_data['user'].username}
        access_token = generate_token(payload, 'access')
        refresh_token = generate_token(payload, 'refresh')
        print(access_token, refresh_token)
        data = {
            'access_token': access_token,
            'refresh_token': refresh_token
        }
        return data
