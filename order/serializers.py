from rest_framework import serializers

from .models import Order, rpOrder



class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = (
            "id",
            "first_name",
            "last_name",
            "email",
            "address",
            "city",
            "state",
            "pincode",
            "phone",
            "book_name",
            "mrp",
            "rent",
            "deposit",
            "type",
            "rental_period",
            "thumbnail",
            "payment",
            "total",
        )
    
    def create(self, validated_data):
        order = Order.objects.create(**validated_data)
        return order

class rpOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = rpOrder
        fields = (
            "id",
            "order_id",
        )

        