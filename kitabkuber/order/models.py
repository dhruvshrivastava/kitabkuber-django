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
    book_name = models.CharField(max_length=20000)
    mrp = models.IntegerField()
    rent = models.IntegerField()
    deposit = models.IntegerField()
    type = models.CharField(max_length=10)
    rental_period = models.CharField(max_length=10)
    thumbnail = models.CharField(max_length=200000)
    payment = models.CharField(max_length=5000)
    total = models.IntegerField()

    class Meta:
        ordering = ['-created_at',]
    
    def __str__(self):
        return self.first_name + ' ' + self.last_name

class rpOrder(models.Model):
    user = models.ForeignKey(User, related_name='rp_order', on_delete=models.CASCADE)
    order_id = models.CharField(max_length=2000000)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta: 
        ordering = ['-created_at',]


