from rest_framework import serializers
from .models import Textbook, User, Order 

class TextbookSerializer(serializers.ModelSerializer):
    seller = serializers.ReadOnlyField(source='seller.username')
    class Meta:
        model = Textbook
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email') # Select desired fields

class OrderSerializer(serializers.ModelSerializer):
    buyer = serializers.ReadOnlyField(source='buyer.username')
    textbook = serializers.ReadOnlyField(source='textbook.title')
    class Meta:
        model = Order
        fields = '__all__'
