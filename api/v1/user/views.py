from rest_framework.generics import RetrieveDestroyAPIView

from apps.user.models import User
from .serializers import UserSerializer


class UserRetrieveDestroyView(RetrieveDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
