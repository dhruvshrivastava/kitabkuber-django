from django.contrib import admin
from .models import Order, RazorpayOrder

admin.site.register(Order)
admin.site.register(RazorpayOrder)
