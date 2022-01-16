from django.conf import settings
from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import render

from rest_framework import status, authentication, permissions
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Order, RazorpayOrder
from .serializers import MyOrderItemSerializer, MyOrderSerializer, OrderSerializer, RazorpayOrderSerializer
import razorpay
from django.core.servers.basehttp import WSGIServer

import os 

@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def checkout(request):
    serializer = OrderSerializer(data=request.data)

    if serializer.is_valid(): 
            paid_amount = sum(item.get('quantity') * item.get('book').price for item in serializer.validated_data['items'])
            try:
                serializer.save(user=request.user, paid_amount=paid_amount)

                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except Exception:
                print(serializer.errors)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    print(serializer.errors)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def create_razorpay_order(request):
    serializer = RazorpayOrderSerializer(data=request.data)
    
    if serializer.is_valid(): 
        amount = request.data["total"]
        try:
            razorpay_client = razorpay.Client(auth=(os.environ["KEY_ID"], os.environ["KEY_SECRET"]))
            razorpay_order = razorpay_client.order.create(dict(amount=amount,
                                                            currency='INR',
                                                            payment_capture='0'))
            razorpay_order_id = razorpay_order['id']
            WSGIServer.handle_error = lambda *args, **kwargs: None
            print(razorpay_order_id)

            serializer.save(user=request.user, order_id = razorpay_order_id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception:
                print(serializer.errors)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    print(serializer.errors)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class OrdersList(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        orders = Order.objects.filter(user=request.user)
        serializer = MyOrderSerializer(orders, many=True)
        return Response(serializer.data)