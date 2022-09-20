from django.shortcuts import get_object_or_404
from rest_framework.generics import RetrieveAPIView, ListAPIView

from apps.account.models import Account, AccountAsset
from .serializers import AccountSerializer, AccountAssetSerializer


class AccountRetrieveDestroyView(RetrieveAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class AccountAssetListView(ListAPIView):
    serializer_class = AccountAssetSerializer

    def get_queryset(self):
        account = get_object_or_404(Account, id=self.kwargs['pk'])
        return AccountAsset.objects.filter(account=account)
