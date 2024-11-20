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

class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class OrderSerializer(serializers.ModelSerializer):
    buyer = serializers.ReadOnlyField(source='buyer.username')
    textbook = serializers.ReadOnlyField(source='textbook.title')
    class Meta:
        model = Order
        fields = '__all__'

