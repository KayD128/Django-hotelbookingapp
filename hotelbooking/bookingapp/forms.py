from tkinter import Label
from django import forms
from django.contrib.auth.models import User
from .models import Booking_table, Room_table

class rooms_form(forms.ModelForm):
    class Meta:
        model = Room_table
        fields = [
            'number_of_rooms',
            'room_price'
        ]

class add_rooms(forms.Form):
    room_name = forms.CharField(required=True, label="Enter the new rooms")
    no_of_rooms = forms.IntegerField(required=True, label="How many Rooms?")
    amount = forms.CharField(required=True, label="Amount")

class booking_form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs)
        self.fields["first_name"].widget.attrs.update({
            'class' : "form-control",
            "id" : "name",
            "type" : "text", 
            "placeholder" : "Your First Name",
            "required" : "required",
            "data-validation-required-message" : "Please enter your name."
        })
        self.fields["last_name"].widget.attrs.update({
            'class' : "form-control", 
            'id' : "name", 
            'type' : "text",  
            'placeholder' : "Your Last Name", 
            'required' : "required",
            'data-validation-required-message' : "Please enter your name."
        })
        self.fields["mail"].widget.attrs.update({
            'class' : "form-control", 
            'id' : "email",
            'type' : "email", 
            'placeholder' : "Your Email", 
            'required' : "required", 
            'data-validation-required-message':"Please enter your email address."
        })
        self.fields["phone_number"].widget.attrs.update({
            'class':"form-control", 
            'id':"name", 
            'type' : "tel", 
            'placeholder' : "Your Phone Number", 
            'data-validation-required-message' : "Please enter your phone number."
        })
        self.fields['phone_number'].required = False

        self.fields["number_of_adult"].widget.attrs.update({
            'class' : "form-control",
            'id' : "adult1", 
            'placeholder' : "How many Adults?",
            'required' : "required"
        })
        self.fields["number_of_children"].widget.attrs.update({
            'class':"form-control",
            'id' : "child1", 
            'placeholder': "How many Children?",
        })
        self.fields['number_of_children'].required = False

        self.fields["rooms"].widget.attrs.update({
            'class':"form-control",
            'id' : "room",  
            'placeholder': "Pick a room",
            'required' : "required"
        })
        self.fields["comment_given"].widget.attrs.update({
            'class' : "form-control", 
            'id' : "request", 
            'placeholder' : "Add any Special Request"
        })
        self.fields['comment_given'].required = False

        self.fields["room_key"].widget.attrs.update({
            'class' : "form-control", 
            'id' : "request", 
            'placeholder' : "Enter a 4-digit PIN only you know about"
        })

    class Meta:
        model = Booking_table
        widgets = {
            'potential_check_in':forms.DateInput(attrs={
                'type':'date', 'class':"form-control", 'id' : "checkIn", 'required' : "required", 'placeholder': "Check In",}),
            'potential_check_out':forms.DateInput(attrs={
                'type':'date', 'class':"form-control", 'id' : "checkOut", 'placeholder': "Check Out",})
        }
        fields = [ 
            'first_name',
            'last_name',
            'mail',
            'phone_number',
            'potential_check_in',
            'potential_check_out',
            'number_of_adult',
            'number_of_children',
            'rooms',
            'comment_given',
            'room_key'
        ]

        
