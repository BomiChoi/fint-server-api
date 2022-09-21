from django.urls import path

from .views import DepositValidateView

urlpatterns = [
    path('/validate', DepositValidateView.as_view()),
]
