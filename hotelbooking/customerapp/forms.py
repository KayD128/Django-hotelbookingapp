from django import forms
from .models import Contact

class Contact_form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["name"].widget.attrs.update({
            'class':"form-control",
            'id':"name",
            'type':"text",
            'placeholder':"Your Name",
            "data-validation-required-message":"Please enter your name."
        })
        self.fields['name'].required = False


        self.fields["mail"].widget.attrs.update({
            "class":"form-control",
            "id":"email",
            "type":"email",
            "placeholder":"Your Email",
            "data-validation-required-message":"Please enter your email address."
        })
        self.fields['mail'].required = False

        self.fields["phone"].widget.attrs.update({
            'class':"form-control",
            'id':"phone",
            'type':"tel",
            'placeholder':"Your Phone Number",
            "data-validation-required-message" : "Please enter your phone number."
        })
        self.fields['phone'].required = False

        self.fields["message"].widget.attrs.update({
            "class":"form-control",
            "id":"message",
            "placeholder":"Your Message",
            "required":"required",
            "data-validation-required-message":"Please enter a message."
        })

    class Meta:
        model = Contact
        fields = [
            'name',
            'mail',
            'phone',
            'message'
        ]