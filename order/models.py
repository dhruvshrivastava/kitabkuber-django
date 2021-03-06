from django.db import models
from django.contrib.auth.models import User

from books.models import Book

class Order(models.Model):
    user = models.ForeignKey(User, related_name='order', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=20000)
    city = models.CharField(max_length=2000)
    state = models.CharField(max_length=2000)
    pincode = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    paid_amount = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)

    class Meta:
        ordering = ['-created_at',]
    
    def __str__(self):
        return self.first_name + ' ' + self.last_name

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    book = models.ForeignKey(Book, related_name='items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return '%s' % self.id

class RazorpayOrder(models.Model):
    user = models.ForeignKey(User, related_name='razorpay_order', on_delete=models.CASCADE)
    order_id = models.CharField(max_length=100000)

    def __str__(self):
        return '%s' % self.order_id