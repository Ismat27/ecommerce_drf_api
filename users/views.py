from rest_framework import generics
from django.contrib.auth import get_user_model

from .serializers import UserRegisterSerializer, UserSerializer

User = get_user_model()
# Create your views here.

class UserCreationApi(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer


class UserDetailApi(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    lookup_field = 'pk'
    queryset = User.objects.all()