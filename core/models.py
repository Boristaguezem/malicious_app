from django.db import models

from accounts.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class Address(models.Model):
    street_number = models.CharField(max_length=255, blank=True)
    address_line1 = models.CharField(max_length=255, blank=True)
    address_line2 = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=60, blank=True)
    region = models.CharField(max_length=60, blank=True)
    postal_code = models.CharField(max_length=60, blank=True)
    country = models.CharField(max_length=90, blank=True)
    is_default = models.BooleanField(default=False)
    
class Category(models.Model):
    parent = models.ForeignKey('self', related_name='childrens', on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length= 255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(default=None, null=True, blank=True)


class OrderStatus(models.Model):
    STATUS_CHOICES = [
        ('Ordered', 'Ordered'),
        ('In Transit', 'In Transit'),
        ('Delivered', 'Delivered'),
        ('Cancelled', 'Cancelled'),
    ]
    status = models.CharField(max_length=12, choices = STATUS_CHOICES)
    updated_at = models.DateTimeField(auto_now = True)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(default=None, null=True, blank=True)
    

    
class Product(models.Model):
    category = models.ManyToManyField(Category, related_name="products")
    name = models.CharField(max_length = 255)
    description = models.TextField(blank=True)
    color = models.CharField(max_length = 255, blank=True)
    size = models.IntegerField()
    fragrance = models.CharField(max_length = 255, blank=True)
    volume = models.DecimalField(max_digits =3, decimal_places =2)
    SKU = models.CharField(max_length=255)
    qty_in_stock = models.IntegerField()
    price = models.DecimalField(max_digits=20, decimal_places=2)
    discount = models.DecimalField(max_digits=3, decimal_places=2, validators=[MinValueValidator(limit_value=0.01),  # Exclusive lower bound
    MaxValueValidator(limit_value=1.00),  # Exclusive upper bound
    ]) #add validation to be 0>x<1
    restock_level = models.IntegerField() #when bellow 10 by default
    updated_at = models.DateTimeField(auto_now = True)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(default=None, null=True, blank=True)
    
class ProductImage(models.Model):
    image = models.ImageField(upload_to='Products/')
    image_url = models.CharField(max_length=255, default=None, blank=True)
    project = models.ForeignKey(Product, related_name='images', on_delete=models.SET_NULL, null=True)
    updated_at = models.DateTimeField(auto_now = True)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(default=None, null=True, blank=True)
    
class Order(models.Model):
    payment_methods = (
        ('paypal', 'PayPal'),
        ('card', 'Card'),
        ('stripe', 'Stripe'),
        ('momo', 'MoMo'),
        ('om','OM')
    )
    user = models.ForeignKey(User, related_name='orders', on_delete=models.SET_NULL, null=True)
    products = models.ManyToManyField(Product, related_name="orders", through='OrderLine')
    shipping_address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True)
    shipping_fees = models.DecimalField(max_digits=20, decimal_places=2)
    total_cost = models.DecimalField(max_digits=20, decimal_places=2)
    status =  models.ForeignKey(OrderStatus, on_delete=models.SET_NULL, null=True)
    payment_method = models.CharField(choices=payment_methods, default="card", max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)
    deleted_at = models.DateTimeField(default=None, null=True, blank=True)
    
    
class OrderLine(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    qty = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(default=None, null=True, blank=True)
    
class Review(models.Model):
    rate_number = (
        (0, ''),
        (1, ''),
        (2, ''),
        (3, ''),
        (4, ''),
        (5,'')
    )
    user = models.ForeignKey(User, related_name='reviews', on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, related_name="reviews", on_delete=models.SET_NULL, null=True)
    rate = models.IntegerField(choices=rate_number, default=0) #add choices to rate choices: Iterable[tuple[_I@IntegerField,
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(default=None, null=True, blank=True)
    
class Cart (models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, related_name="cart")
    products = models.ManyToManyField(Product, through="CartItem")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    Deleted_at = models.DateTimeField(default=None, null=True, blank=True)
    
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    qty = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    Deleted_at = models.DateTimeField(default=None, null=True, blank=True)
