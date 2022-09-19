from django.urls import path

from .views import UserRetrieveDestroyView

urlpatterns = [
    path('/<int:pk>', UserRetrieveDestroyView.as_view()),
]
