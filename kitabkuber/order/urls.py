from django.urls import path

from order import views

urlpatterns = [
    path('checkout/', views.checkout),
    path('orders/', views.OrdersList.as_view()),
    path('add_to_cart/', views.add_to_cart),
    path('cart/', views.CartList.as_view()),


]