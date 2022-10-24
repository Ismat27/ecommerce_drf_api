from rest_framework import generics
from .models import Cart
from .serializers import CartSerializer, CartUpdateSerializer
# Create your views here.

class CartRetrieveUpdate(generics.RetrieveUpdateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    # def perform_update()

    def get_serializer_class(self):
        if self.request.method == 'PUT' or self.request.method == 'PATCH':
            return CartUpdateSerializer
        return super().get_serializer_class()

