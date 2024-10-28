from rest_framework import serializers
from .models import CartItem
from .models import Cart
from .models import Review
from .models import OrderLine
from .models import Order
from .models import ProductImage
from .models import Product
from .models import Address
from .models import Category
from .models import OrderStatus

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['id', 'street_number', 'address_line1', 'address_line2', 'city', 'region', 'postal_code', 'country', 'is_default']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'parent', 'name', 'description', 'created_at', 'updated_at', 'deleted_at']


class OrderStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderStatus
        fields = ['id', 'status', 'created_at', 'updated_at', 'deleted_at']

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'category', 'name', 'description', 'color', 'size', 'fragrance', 'volume', 'SKU',
                  'qty_in_stock', 'price', 'discount', 'restock_level', 'created_at', 'updated_at', 'deleted_at']


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id', 'image', 'image_url', 'project', 'created_at', 'updated_at', 'deleted_at']



class OrderSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'user', 'products', 'shipping_address', 'shipping_fees', 'total_cost', 'status', 'payment_method', 'created_at', 'updated_at', 'deleted_at']



class OrderLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderLine
        fields = ['id', 'product', 'order', 'qty', 'created_at', 'updated_at', 'deleted_at']



class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'user', 'product', 'rate', 'comment', 'created_at', 'updated_at', 'deleted_at']



class CartSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = ['id', 'user', 'products', 'created_at', 'updated_at', 'Deleted_at']



class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['id', 'cart', 'product', 'qty', 'created_at', 'updated_at', 'Deleted_at']


