from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from .serializers import UserRegisterSerializer, UserSerializer

User = get_user_model()
# Create your views here.

class UserCreationApi(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer


class UserDetailApi(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    lookup_field = 'pk'
    queryset = User.objects.all()

class UserLogin(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email,
            'is_admin': user.is_admin,
            'first_name': user.first_name,
            'last_name': user.last_name,
        })
