from rest_framework import serializers

from .models import Product

class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ProductSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    desc = serializers.CharField()
    price = serializers.DecimalField(max_digits=15, decimal_places=2)
    discount = serializers.SerializerMethodField(read_only=True)
    image = serializers.ImageField()

    def get_discount(self, obj):
        return "%.2f" %(float(obj.price) * 0.2)