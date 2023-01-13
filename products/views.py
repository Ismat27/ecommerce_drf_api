from rest_framework import generics, permissions
from rest_framework.parsers import MultiPartParser, FormParser

from .serializers import ProductSerializer, ProductCreateSerializer
from .models import Product
# Create your views here.

class ProductListCreate(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    parser_classes = [MultiPartParser, FormParser]

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return ProductCreateSerializer
        return super().get_serializer_class()

    # def perform_create(self, serializer):
    #     print(serializer.validated_data['price'])
    #     serializer.save()
        # return super().perform_create(serializer)

class ProductRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def get_permissions(self):
        if self.request.method != 'GET':
            return  [permissions.IsAdminUser()]
        return super().get_permissions()
