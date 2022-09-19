from django.urls import path

from .views import AccountRetrieveDestroyView

urlpatterns = [
    path('/<int:pk>', AccountRetrieveDestroyView.as_view())
]
