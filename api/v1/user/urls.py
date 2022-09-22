from django.urls import path

from .views import UserRetrieveView, MeRetrieveView, LoginView

urlpatterns = [
    path('/<int:pk>', UserRetrieveView.as_view()),
    path('/me', MeRetrieveView.as_view()),
    path('/login', LoginView.as_view())
]
