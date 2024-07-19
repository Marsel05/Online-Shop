from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()


class Supplier(models.Model):
    name = models.CharField(max_length=100)
    contact_name = models.CharField(max_length=100)
    contact_email = models.CharField(max_length=100)
    contact_phone = models.CharField(max_length=100)
    address = models.CharField(max_length=100)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    phone = models.PositiveIntegerField(default=0)
    address = models.CharField(max_length=100)
    supplier = models.OneToOneField(Supplier, on_delete=models.CASCADE)

class Product(models.Model):
    name = models.CharField(max_length=100 )
    description = models.TextField()
    price = models.PositiveIntegerField(default=0)
    stock = models.IntegerField(default=0)
    sku = models.CharField(max_length=100, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)


class Order(models.Model):
    order_number = models.CharField(max_length=100, unique=True)
    order_date = models.DateTimeField()
    total_amount = models.PositiveIntegerField(default=0)
    CHOICES_STATUS = (
        ('в обработке', 'в обработке'),
        ('доставлен', 'доставлен')
    )
    status = models.CharField(choices=CHOICES_STATUS, max_length=100)


class OrderItem(models.Model):
    product_name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField(default=0)
    unit_price = models.PositiveIntegerField(default=0)
    total_price = models.PositiveIntegerField(default=0)


class Payment(models.Model):
    payment_date = models.DateTimeField()
    amount = models.PositiveIntegerField(default=0)
    payment_method = models.CharField(max_length=100)
    transaction_id = models.CharField(max_length=100, unique=True)


class Review(models.Model):
    product_name = models.CharField(max_length=100)
    review_text = models.TextField()
    rating = models.CharField(max_length=100, choices=[(i, str(i)) for i in range(1,6)])
    review_date = models.DateField(auto_now_add=True)



