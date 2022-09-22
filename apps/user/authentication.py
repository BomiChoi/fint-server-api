import datetime
import os

import jwt
from django.shortcuts import get_object_or_404
from rest_framework import exceptions
from rest_framework.authentication import TokenAuthentication

from apps.user.models import User


class JSONWebTokenAuthentication(TokenAuthentication):
    def authenticate_credentials(self, key):
        try:
            payload = jwt.decode(key, os.getenv('JWT_SECRET_KEY'), os.getenv('JWT_ALGORITHM'))
            user = get_object_or_404(User, username=payload['username'])
        except jwt.DecodeError:
            raise exceptions.AuthenticationFailed('Invalid token')
        except jwt.ExpiredSignatureError:
            raise exceptions.AuthenticationFailed('Token has expired')
        if not user.is_active:
            raise exceptions.AuthenticationFailed('User inactive or deleted')
        return user, payload


def generate_token(payload, type):
    if type == "access":
        # 2시간
        exp = datetime.datetime.utcnow() + datetime.timedelta(hours=2)
    elif type == "refresh":
        # 2주
        exp = datetime.datetime.utcnow() + datetime.timedelta(weeks=2)
    else:
        raise Exception("Invalid tokenType")

    payload['exp'] = exp
    payload['iat'] = datetime.datetime.utcnow()
    encoded = jwt.encode(payload, os.getenv('JWT_SECRET_KEY'), algorithm=os.getenv('JWT_ALGORITHM'))

    return encoded
