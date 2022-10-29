from django.shortcuts import get_object_or_404
from rest_framework import serializers
from products.serializers import ProductSerializer
from .models import Cart, CartItem
from products.models import Product

class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(source='item', read_only=True)
    class Meta:
        model = CartItem
        fields = [
            'quantity',
            'product',
            'amount'
        ]

class CartSerializer(serializers.ModelSerializer):
    cart_items = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Cart
        fields = [
            'cart_items',
            'total_amount',
            # 'is_ordered'
        ]

    def get_cart_items(self, obj):
        items = obj.cart_items
        serializer = CartItemSerializer(items, many=True)
        return serializer.data

    def get_total_amount(self, obj):
        amt = obj.total_amount
        return amt

class CartUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cart
        fields = [
            'is_ordered'
        ]

class AddToCartSerializer(serializers.Serializer):
    product = ProductSerializer(source='item', read_only=True)
    quantity = serializers.IntegerField(default=1)
    product_id = serializers.IntegerField(write_only=True)

    def create(self, validated_data):
        item = get_object_or_404(Product, pk=validated_data['product_id'])
        new_item = CartItem.objects.create(
            quantity = validated_data['quantity'],
            item = item
        )
        return new_item