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
    discounted_price = serializers.DecimalField(max_digits=15, decimal_places=2)
    discount = serializers.SerializerMethodField(read_only=True)
    in_stock = serializers.BooleanField()
    is_flash_sale = serializers.BooleanField()
    is_recommended = serializers.BooleanField()
    timestamp = serializers.SerializerMethodField(read_only=True)
    stock_quantity = serializers.IntegerField()
    id = serializers.SerializerMethodField(read_only=True)
    image = serializers.ImageField()
    category = serializers.SerializerMethodField()
    brand = serializers.SerializerMethodField()

    def get_discount(self, obj):
        try:
            price = obj.price
            discounted_price = obj.discounted_price
            diff = price - discounted_price
            return round(diff / price * 100)
        except Exception:
            return 0

    def get_id(self, obj):
        return obj.id
    
    def get_category(self, obj):
        if obj.category:
            return obj.category.name
        return ""

    def get_brand(self, obj):
        if obj.brand:
            return obj.brand.name
        return ""

    def get_timestamp(self, obj):
        return obj.updated_at.timestamp() * 1000
