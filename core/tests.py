from django.test import TestCase
from .models import Address, Category, OrderStatus, Product, ProductImage, Order, OrderLine, Review, Cart, CartItem
from .serializers import AddressSerializer, CategorySerializer, OrderStatusSerializer, ProductSerializer, ProductImageSerializer, OrderSerializer, OrderLineSerializer, ReviewSerializer, CartSerializer, CartItemSerializer

class SerializerTestCase(TestCase):

    def test_address_serializer(self):
        address = Address.objects.create(street_number="123", address_line1="Main St", city="Springfield", region="IL", postal_code="62701", country="USA")
        serializer = AddressSerializer(address)
        self.assertEqual(serializer.data['street_number'], "123")
        self.assertEqual(serializer.data['city'], "Springfield")

    def test_category_serializer(self):
        category = Category.objects.create(name="Electronics", description="Gadgets and devices")
        serializer = CategorySerializer(category)
        self.assertEqual(serializer.data['name'], "Electronics")

    def test_order_status_serializer(self):
        order_status = OrderStatus.objects.create(status="Ordered")
        serializer = OrderStatusSerializer(order_status)
        self.assertEqual(serializer.data['status'], "Ordered")

    def test_product_serializer(self):
        category = Category.objects.create(name="Clothing")
        product = Product.objects.create(
            name="T-shirt",
            size=42,
            volume=1.00,
            SKU="TSH123",
            qty_in_stock=100,
            price=20.00,
            discount=0.10,  # Added discount value
            restock_level=5
        )
        product.category.add(category)
        serializer = ProductSerializer(product)
        self.assertEqual(serializer.data['name'], "T-shirt")
        self.assertEqual(serializer.data['qty_in_stock'], 100)

    def test_product_image_serializer(self):
        product = Product.objects.create(
            name="T-shirt",
            size=42,
            volume=1.00,
            SKU="TSH123",
            qty_in_stock=100,
            price=20.00,
            discount=0.10,  # Added discount value
            restock_level=5
        )
        product_image = ProductImage.objects.create(image_url="image1.jpg", project=product)
        serializer = ProductImageSerializer(product_image)
        self.assertEqual(serializer.data['image_url'], "image1.jpg")

    def test_order_serializer(self):
        order = Order.objects.create(shipping_fees=5.00, total_cost=100.00)
        serializer = OrderSerializer(order)
        self.assertEqual(serializer.data['shipping_fees'], "5.00")

    def test_order_line_serializer(self):
        product = Product.objects.create(
            name="T-shirt",
            size=42,
            volume=1.00,
            SKU="TSH123",
            qty_in_stock=100,
            price=20.00,
            discount=0.10,  # Added discount value
            restock_level=5
        )
        order = Order.objects.create(shipping_fees=5.00, total_cost=100.00)
        order_line = OrderLine.objects.create(product=product, order=order, qty=2)
        serializer = OrderLineSerializer(order_line)
        self.assertEqual(serializer.data['qty'], 2)

    def test_review_serializer(self):
        review = Review.objects.create(rate=5, comment="Excellent product")
        serializer = ReviewSerializer(review)
        self.assertEqual(serializer.data['rate'], 5)
        self.assertEqual(serializer.data['comment'], "Excellent product")

    def test_cart_serializer(self):
        cart = Cart.objects.create()
        serializer = CartSerializer(cart)
        self.assertEqual(serializer.data['id'], cart.id)

    def test_cart_item_serializer(self):
        product = Product.objects.create(
            name="T-shirt",
            size=42,
            volume=1.00,
            SKU="TSH123",
            qty_in_stock=100,
            price=20.00,
            discount=0.10,  # Added discount value
            restock_level=5
        )
        cart = Cart.objects.create()
        cart_item = CartItem.objects.create(cart=cart, product=product, qty=2)
        serializer = CartItemSerializer(cart_item)
        self.assertEqual(serializer.data['qty'], 2)
