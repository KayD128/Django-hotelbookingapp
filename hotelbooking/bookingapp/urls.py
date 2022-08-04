from django.urls import re_path
from hotelbooking.bookingapp import views as book_view

urlpatterns = [
    re_path(r'^booking/', book_view.booking_room, name='booking'),
    re_path(r'^add_room/', book_view.add_room, name='addRoom'),
    re_path(r'^view_check_in/', book_view.view_check_in, name="checkinView"),
    re_path(r'^check_in/(?P<check_in_id>\d+)/', book_view.check_in, name="check_in"),
    re_path(r'^view_check_out/', book_view.view_check_out, name="checkoutView"),
    re_path(r'^check_out/(?P<check_out_id>\d+)/', book_view.check_out, name="check_out"),
    re_path(r'^show_rooms/', book_view.show_rooms, name="showRooms"),
    re_path(r'^edit_room/(?P<room_id>\d+)/', book_view.edit_room, name='edit_room'),
    re_path(r'^view_receipt/(?P<book_me_id>\d+)/', book_view.receipt, name='viewReceipt'),
]