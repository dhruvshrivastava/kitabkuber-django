from rest_framework import serializers

from .models import Order, OrderItem, Cart, CartItem

from books.serializers import BookSerializer

class MyOrderItemSerializer(serializers.ModelSerializer):    
    book = BookSerializer()

    class Meta:
        model = OrderItem
        fields = (
            "mrp",
            "rent",
            "deposit",
            "book",
            "rental_plan",
        )

class MyOrderSerializer(serializers.ModelSerializer):
    items = MyOrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = (
            "id",
            "first_name",
            "last_name",
            "email",
            "address",
            "pincode",
            "place",
            "phone",
            "items",
            "paid_amount",
        )

class OrderItemSerializer(serializers.ModelSerializer):    
    class Meta:
        model = OrderItem
        fields = (
            "mrp",
            "rent",
            "deposit",
            "book",
            "rental_plan",
        )

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = (
            "id",
            "first_name",
            "last_name",
            "email",
            "address",
            "pincode",
            "phone",
            "items",
        )
    
    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)

        for item_data in items_data:
            OrderItem.objects.create(order=order, **item_data)
            
        return order

class MyCartItemSerializer(serializers.ModelSerializer):    
    book = BookSerializer()

    class Meta:
        model = CartItem
        fields = (
            "book",
            "rental_plan",
        )


class MyCartSerializer(serializers.ModelSerializer):
    items = MyCartItemSerializer(many=True)

    class Meta:
        model = Cart
        fields = (
            "id",
            "total_payable",
            "number_of_items",
            "cart_items",

        )

class CartItemSerializer(serializers.ModelSerializer):    
    class Meta:
        model = CartItem
        fields = (
            "book",
            "rental_plan",
        )

class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True)

    class Meta:
        model = Cart
        fields = (
            "id",
            "total_payable",
            "number_of_items",
            "cart_items",

        )
    
    def create(self, validated_data):
        items_data = validated_data.pop('cart_items')
        cart = Cart.objects.create(**validated_data)

        for item_data in items_data:
            CartItem.objects.create(cart=cart, **item_data)
            
        return cart