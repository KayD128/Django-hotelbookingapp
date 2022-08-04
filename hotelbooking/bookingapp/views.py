from xml.etree.ElementTree import Comment
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from numpy import number
from django.contrib import messages
from hotelbooking.bookingapp.forms import rooms_form, booking_form, add_rooms
from hotelbooking.bookingapp.models import Booking_table, Room_table, Check_out_table, Check_in_table
from django.http import HttpResponsePermanentRedirect
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from django.db import transaction
import datetime
from django.db.models import F
# Create your views here.

# @login_required
# def add_room(request):
#     if request.method == 'POST':
#         room_form = rooms_form(request.POST)
#         if room_form.is_valid():
#             room_name = room_form.cleaned_data['rooms']
#             room_no = room_form.cleaned_data['number_of_rooms']
#             roomPrice = room_form.cleaned_data['room_price']
#             update_room = Room_table(rooms=room_name, number_of_rooms=room_no, room_price=roomPrice)
#             update_room.save()
#             messages.success(request, ('Your table has been updated successfully'))
#         else:
#             messages.error(request, ("Your updating failed"))
#         return HttpResponsePermanentRedirect(reverse('addRoom'))
#     else:
#         room_form = rooms_form()
#     return render(request, 'bookingapp/edit_rooms_forms.html', {
#         'room_form': room_form})
        # Booking_table.objects.filter(booking_id=check_in_id).update(check_in_time=checked.time(), real_check_in=checked.date())


def show_rooms(request):
    my_rooms = Room_table.objects.all()
    return render(request, 'bookingapp/display_rooms.html',
    {'my_rooms':my_rooms})


@login_required
def edit_room(request, room_id):
    mine = Room_table.objects.all().filter(room_id=room_id).values()[0]
    room_name = mine.get("rooms")

    if request.method == 'POST':
        room = get_object_or_404(Room_table, room_id=room_id)
        room_form = rooms_form(request.POST or None, instance=room)
        if room_form.is_valid():
            room_no = room_form.cleaned_data['number_of_rooms']
            roomPrice = room_form.cleaned_data['room_price']

            Room_table.objects.filter(room_id=room_id, rooms=room_name).update(number_of_rooms=room_no, room_price=roomPrice)
            messages.success(request, ('Your table has been updated successfully'))
        else:
            messages.error(request, ('Please correct the error below.'))
            return HttpResponsePermanentRedirect(reverse('edit_room', args=(room_id,)))
    else:
        room = get_object_or_404(Room_table, room_id=room_id)
        room_form = rooms_form(instance=room)
    return render(request, 'bookingapp/edit_each_rooms.html', {
        'my_form': room_form, 'room_name': room_name
    })

def add_room(request):
    if request.method == 'POST':
        my_form = add_rooms(request.POST)
        if my_form.is_valid():
            roomName = my_form.cleaned_data["room_name"]
            noOfRooms = my_form.cleaned_data["no_of_rooms"]
            price  = my_form.cleaned_data["amount"]
            new_room = Room_table(rooms=roomName, number_of_rooms=noOfRooms, room_price=price)
            new_room.save()
            messages.success(request, ('Your room has been created successfully.'))
            return show_rooms(request)
        else:
            messages.error(request, ("Please correct the error below."))
            return HttpResponsePermanentRedirect(reverse('addRoom'))
    else:
        my_form = add_rooms()
        return render(request, 'bookingapp/edit_rooms_forms.html', {'room_form': my_form})

@transaction.atomic
def booking_room(request):
    # pin = str(random.randint(0000, 9999))
    if request.method == 'POST':
        # user = get_object_or_404(User)
        book_form = booking_form(request.POST)
        if book_form.is_valid():
            firstName = book_form.cleaned_data['first_name']
            lastName = book_form.cleaned_data['last_name']
            email = book_form.cleaned_data['mail']
            phoneNo = book_form.cleaned_data['phone_number']
            checkIn = book_form.cleaned_data['potential_check_in']
            checkOut = book_form.cleaned_data['potential_check_out']
            adult = book_form.cleaned_data['number_of_adult']
            children = book_form.cleaned_data['number_of_children']
            room_type = book_form.cleaned_data['rooms']
            comment = book_form.cleaned_data['comment_given']
            pin = book_form.cleaned_data['room_key']

            roomAccount = Room_table.objects.all().filter(rooms=room_type).values()[0]
            if roomAccount.get("number_of_rooms") <= 0:
                messages.error(request, ('We are sorry. The room picked is not available. You can try another room.'))
                return HttpResponsePermanentRedirect(reverse('booking'))
            else:
            
                book = Booking_table(first_name=firstName, last_name=lastName, mail=email, phone_number=phoneNo, potential_check_in=checkIn, potential_check_out=checkOut, number_of_adult=adult, number_of_children=children, rooms = room_type, comment_given=comment, room_id=roomAccount.get("room_id"), room_key=pin, room_price=roomAccount.get("room_price"))
                book.save()
                    
                check = Check_in_table(first_name=firstName, last_name=lastName, mail=email, phone_number=phoneNo, potential_check_in=checkIn, potential_check_out=checkOut, number_of_adult=adult, number_of_children=children, rooms=room_type, room_id=roomAccount.get("room_id"), key=pin, )
                check.save()

                messages.success(request, ('Your room has been successfully reserved for you. Contact us for any complaint on 07063083133'))
                return HttpResponsePermanentRedirect(reverse('booking',))
        else:
            messages.error(request, ('Correct the error in your field, Please.'))
            return HttpResponsePermanentRedirect(reverse('booking'))
    else:
        book_form = booking_form()
    return render(request, 'bookingapp/booking.html', {
        'book_form': book_form
    })
        
@login_required
def view_check_in(request):
    # pass
    profile_details = Check_in_table.objects.all()
    return render(request, 'bookingapp/check_in.html',
    {'profile_details':profile_details})
    

@transaction.atomic
@login_required
def check_in(request, check_in_id):
    checked = datetime.datetime.now()

    my_details = Check_in_table.objects.filter(check_in_id=check_in_id).values()[0]
    booking_details = Booking_table.objects.filter(booking_id=check_in_id).values()[0]

    check_in = Check_out_table(first_name=my_details.get("first_name"), last_name=my_details.get("last_name"), mail=my_details.get("mail"), phone_number=my_details.get("phone_number"), real_check_in=checked.date(), potential_check_out=my_details.get("potential_check_out"), number_of_adult=my_details.get("number_of_adult"), number_of_children=my_details.get("number_of_children"), rooms=my_details.get("rooms"), room_id=my_details.get("room_id"), key=my_details.get("key"), book_me_id=booking_details.get("booking_id"))
    check_in.save()

    Room_table.objects.all().filter(room_id=my_details.get("room_id")).update(number_of_rooms = F('number_of_rooms') - 1)

    my_checkOut = Check_in_table.objects.filter(check_in_id=check_in_id)
    my_checkOut.delete()
    
    Booking_table.objects.filter(booking_id=check_in_id).update(check_in_time=checked.time(), real_check_in=checked.date())

    return view_check_in(request)
    # pass

    # bookAccount.save()

@login_required
def view_check_out(request):
    profile_details = Check_out_table.objects.all()
    return render(request, 'bookingapp/check_out.html',
    {'profile_details':profile_details})

@transaction.atomic
@login_required
def check_out(request, check_out_id):
    # pass
    checked = datetime.datetime.now()
    get_date = Check_out_table.objects.filter(check_out_id=check_out_id).values()[0]
    # print(get_date)
    Booking_table.objects.filter(booking_id=get_date.get("book_me_id")).update(check_out_time=checked.time(), real_check_out=checked.date())

    Room_table.objects.filter(room_id=get_date.get("room_id")).update(number_of_rooms = F('number_of_rooms') + 1)
    book_details = Booking_table.objects.filter(booking_id=get_date.get("book_me_id")).values()[0]

    number_of_days = book_details.get("real_check_out") - book_details.get("real_check_in")
    roomPrice = number_of_days.days * book_details.get("room_price")
    Booking_table.objects.filter(booking_id=get_date.get("book_me_id")).update(total_price=roomPrice)

   

    return view_check_out(request)


def receipt(request, book_me_id):

    check_out_details = Booking_table.objects.all().filter(booking_id=book_me_id)

    # my_details = Check_out_table.objects.filter(book_me_id=book_me_id)
    # my_details.delete()
    return render(request, 'bookingapp/receipt.html',
    {'check_out_details':check_out_details}) 

    


