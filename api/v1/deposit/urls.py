from django.urls import path

from .views import DepositValidateView, DepositRunView

urlpatterns = [
    path('/validate', DepositValidateView.as_view()),
    path('/run', DepositRunView.as_view()),
]
