from django.conf import settings
from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import render

from rest_framework import status, authentication, permissions
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Order, rpOrder
from .serializers import OrderSerializer, rpOrderSerializer
import razorpay
from django.core.servers.basehttp import WSGIServer

import os 


@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def checkout(request):
    serializer = OrderSerializer(data=request.data)

    if serializer.is_valid(): 
            try:
                serializer.save(user=request.user)

                return Response("Order created")
            except Exception:
                print(serializer.errors)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    print(serializer.errors)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def create_razorpay_order(request):
    amount = request.data["total"]
    razorpay_client = razorpay.Client(auth=(os.environ["KEY_ID"], os.environ["KEY_SECRET"]))
    razorpay_order = razorpay_client.order.create(dict(amount=amount,
                                                       currency='INR',
                                                       payment_capture='0'))
    razorpay_order_id = razorpay_order['id']
    WSGIServer.handle_error = lambda *args, **kwargs: None
    print(razorpay_order_id)
    rpOrder.objects.create(user=request.user, order_id = razorpay_order_id)
    return Response(razorpay_order_id)
    
    
    
    
class OrdersList(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        orders = Order.objects.filter(user=request.user)
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)


class rpOrdersList(APIView):
        authentication_classes = [authentication.TokenAuthentication]
        permission_classes = [permissions.IsAuthenticated]
        def get(self, request):
            orders = rpOrder.objects.filter(user=request.user)
            serializer = rpOrderSerializer(orders, many=True)
            return Response(serializer.data)
            
