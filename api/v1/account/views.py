from rest_framework.generics import RetrieveDestroyAPIView

from apps.account.models import Account
from .serializers import AccountSerializer


class AccountRetrieveDestroyView(RetrieveDestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
