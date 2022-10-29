from rest_framework import generics, permissions
from .models import Cart
from .serializers import CartSerializer, CartUpdateSerializer, AddToCartSerializer
# Create your views here.

class CartRetrieveUpdate(generics.RetrieveUpdateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    # def perform_update()

    def get_serializer_class(self):
        if self.request.method == 'PUT' or self.request.method == 'PATCH':
            return CartUpdateSerializer
        return super().get_serializer_class()

class AddToCartApiView(generics.CreateAPIView):
    serializer_class = AddToCartSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        request = self.request
        user = request.user
        cart = Cart.objects.filter(
            is_ordered=False, user=user
        ).order_by('-last_updated').first()
        if cart is None:
            cart = Cart.objects.create(
                user=user
            )
        instance = serializer.save()
        cart.cartitem_set.add(instance)

