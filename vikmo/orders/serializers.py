from rest_framework import serializers
from .models import Order, OrderItem

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'
        read_only_fields = ('line_total',)

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = '__all__'
        read_only_fields = ('order_number', 'total_amount', 'status')

    def update(self, instance, validated_data):
        if instance.status in ['CONFIRMED', 'DELIVERED']:
            raise serializers.ValidationError(
                "Confirmed or delivered orders cannont be modified."
            )
        return super().update(instance, validated_data)  