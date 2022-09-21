from rest_framework.generics import CreateAPIView

from .serializers import DepositValidateSerializer, DepositRunSerializer


class DepositValidateView(CreateAPIView):
    serializer_class = DepositValidateSerializer


class DepositRunView(CreateAPIView):
    serializer_class = DepositRunSerializer
