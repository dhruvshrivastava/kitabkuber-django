from django.db import models
from django.contrib.auth.models import User

from books.models import Book

class Order(models.Model):
    user = models.ForeignKey(User, related_name='order', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    pincode = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    paid_amount = models.IntegerField()

    class Meta:
        ordering = ['-created_at',]
    
    def __str__(self):
        return self.first_name + ' ' + self.last_name

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    book = models.ForeignKey(Book, related_name ='items', on_delete=models.CASCADE)
    mrp = models.IntegerField()
    deposit = models.IntegerField()
    rent = models.IntegerField()
    rental_plan = models.CharField(max_length=100)

    def __str__(self):
        return '%s' % self.id

        
class Cart(models.Model):
    user = models.ForeignKey(User, related_name='cart', on_delete=models.CASCADE)
    number_of_items = models.IntegerField()
    total_payable = models.IntegerField()

    def __str__(self):
        return self.number_of_items

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='cart_items', on_delete=models.CASCADE)
    book = models.ForeignKey(Book, related_name ='cart_items', on_delete=models.CASCADE)
    rental_plan = models.CharField(max_length=1000)

    def __str__(self):
        return '%s' % self.id 
