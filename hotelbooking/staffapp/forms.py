import email
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, required=False, help_text='Optional'),
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional'),
    email = forms.EmailField(max_length=254, help_text='Enter a valid email address')

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        ]

class User_form(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class myStaff_form(forms.ModelForm):
    profile_passport = forms.ImageField(required=False, label='Profile passport')
    means_of_identity = forms.ImageField(required=False, label='Means of identity')
    particulars = forms.FileField(required=False, label='particulars')
    class Meta:
        model = Profile
        fields = [
            'status',
            'address',
            'phone',
            'nationality',
            'state',
            'means_of_identity',
            'particulars',
            'profile_passport',
            'position',
            'marital_status',
            'staff',
        ]

