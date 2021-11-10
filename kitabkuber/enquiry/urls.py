from django.urls import path
from enquiry import views 


urlpatterns = [
    path("", views.submit_enquiry)

]