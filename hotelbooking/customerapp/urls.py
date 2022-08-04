from django.urls import path, re_path, include
from hotelbooking.customerapp import views as customer_view

urlpatterns = [
    re_path(r'^contact/', customer_view.contact_us, name="contact"),
]