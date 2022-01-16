from django.urls import path

from order import views

urlpatterns = [
    path('checkout/', views.checkout),
    path('orders/', views.OrdersList.as_view()),
    path('create-rp-order/', views.create_razorpay_order),




]