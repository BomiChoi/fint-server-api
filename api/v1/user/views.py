from rest_framework.generics import RetrieveAPIView, CreateAPIView

from apps.user.models import User
from .serializers import UserSerializer, LoginSerializer


class UserRetrieveView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class MeRetrieveView(RetrieveAPIView):
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class LoginView(CreateAPIView):
    serializer_class = LoginSerializer
