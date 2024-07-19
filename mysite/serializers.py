from .models import *
from rest_framework import serializers


class UserProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class OrderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class OrderItemSerializers(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'

class PaymentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model =Review
        fields = '__all__'

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model =Category
        fields = '__all__'

class SupplierSerializers(serializers.ModelSerializer):
    class Meta:
        model =Supplier
        fields = '__all__'

