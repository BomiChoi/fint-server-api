from rest_framework.generics import CreateAPIView

from .serializers import DepositValidateSerializer


class DepositValidateView(CreateAPIView):
    serializer_class = DepositValidateSerializer
