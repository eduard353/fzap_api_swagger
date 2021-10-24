from rest_framework import serializers
from .models import Mark, Model, Order, Shop, Answer


class MarkSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    mark_name = serializers.CharField(max_length=50)
    mark_full_name = serializers.CharField(max_length=100)
    class Meta:
        model = Mark
        fields = ('id', 'mark_name', 'mark_full_name')

class ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Model
        fields = ('id', 'mark', 'model_name')

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'user', 'model', 'year', 'vin', 'order_details', 'date')

class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ('id', 'shop_name', 'address', 'phone', 'email', 'description')

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('id', 'order', 'shop', 'answer_details', 'price', 'date')
