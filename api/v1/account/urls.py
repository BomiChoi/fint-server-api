from django.urls import path

from .views import AccountRetrieveDestroyView, AccountAssetListView

urlpatterns = [
    path('/<int:pk>', AccountRetrieveDestroyView.as_view()),
    path('/<int:pk>/assets', AccountAssetListView.as_view())
]
