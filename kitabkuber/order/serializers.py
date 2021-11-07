from rest_framework import serializers

from .models import Order



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
            "thumbnail"
        )
    
    def create(self, validated_data):
        order = Order.objects.create(**validated_data)
        return order