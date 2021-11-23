from django.urls import path
from enquiry import views 


urlpatterns = [
    path("enquiry", views.submit_enquiry),

]