# from typing_extensions import Required
from django.shortcuts import render, get_object_or_404
# from hotelbooking import staffapp
from .forms import SignUpForm, myStaff_form, User_form
from django.urls import reverse_lazy, reverse
from django.views import generic
from .models import Profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import transaction
from django.contrib import messages
from django.http import HttpResponsePermanentRedirect, HttpResponseRedirect

# Create your views here.
class SignUpView(generic.CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

@login_required
def manage_staff(request):
    staff_details = Profile.objects.all().filter(staff=True)
    return render(request, 'staffapp/manage_staff.html', 
    {'staff':staff_details})

@login_required
def manage_customer(request):
    customer_details = Profile.objects.all().filter(staff=False)
    return render(request, 'staffapp/manage_customer.html', {'customer_details': customer_details})

@login_required
def staff_profile(request, user_id):
    myProfile = Profile.objects.all().filter(user_id=user_id)
    return render(request, 'staffapp/staff_profile.html', {'myProfile':myProfile})

@login_required
@transaction.atomic
def edit_profile(request, user_id):
    if request.method == 'POST':
        user = get_object_or_404(User, id=user_id)
        user_form = User_form(request.POST, instance=user)
        profile_form = myStaff_form(request.POST or None, request.FILES or None, instance=user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            if profile_form.cleaned_data['staff']:
                user.is_staff = True
                user.save()
            else:
                user.is_staff = False
                user.save()
            messages.success(request, ('Your profile was successfully updated!'))
            staff_profile(request, user_id)
        else:
            messages.error(request, ('Please correct the error below.'))
            return HttpResponsePermanentRedirect(reverse('edit_profile', args=(user_id,)))
    else:
        user = get_object_or_404(User, id=user_id)
        user_form = User_form(instance=user)
        profile_form = myStaff_form(instance=user.profile)
    return render(request, 'staffapp/staff_edit_profile_form.html', {
        'user_form': user_form,
        'profile_form': profile_form     
    })

@login_required
def deactivate_staff(request, user_id):
    user = User.objects.get(id=user_id)
    if user.is_active:
        user.is_active = 0
    else:
        user.is_active = 1
    user.save()
    return staff_profile(request, user_id)


