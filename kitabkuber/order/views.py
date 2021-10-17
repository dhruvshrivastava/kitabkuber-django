from django.conf import settings
from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import render

from rest_framework import status, authentication, permissions
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Order, OrderItem, Cart, CartItem
from .serializers import OrderSerializer, MyOrderSerializer, CartSerializer, MyCartSerializer

@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def checkout(request):
    serializer = OrderSerializer(data=request.data)

    if serializer.is_valid():
        paid_amount = 0
        for item in serializer.validated_data['items']:
            if item.get('rental_plan') == 'Yearly':
                paid_amount += item.get('mrp')
            if item.get('rental_plan') == 'Monthly':
                paid_amount += item.get('deposit')

        try:
            serializer.save(user=request.user, paid_amount=paid_amount)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OrdersList(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        orders = Order.objects.filter(user=request.user)
        serializer = MyOrderSerializer(orders, many=True)
        return Response(serializer.data)

@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def add_to_cart(request):
    serializer = CartSerializer(data=request.data)

    if serializer.is_valid():
        total_payable = 0
        for item in serializer.validated_data['cart_items']:
            if item.get('rental_plan') == 'Yearly':
                total_payable += item.get('mrp')
            if item.get('rental_plan') == 'Monthly':
                total_payable += item.get('deposit')

        try:
            serializer.save(user=request.user, total_payable=total_payable)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CartList(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        cart = Cart.objects.filter(user=request.user)
        serializer = MyCartSerializer(cart, many=True)
        return Response(serializer.data)