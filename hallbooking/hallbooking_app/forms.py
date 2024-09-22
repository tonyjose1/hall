# hallbooking_app/forms.py
from django import forms
from .models import Hall, UserContact
from .models import Booking

class HallForm(forms.ModelForm):
    class Meta:
        model = Hall
        fields = ['name', 'capacity', 'location', 'description', 'amenities']

class UserContactForm(forms.ModelForm):
    class Meta:
        model = UserContact
        fields = ['name', 'number', 'address', 'email']


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['hall', 'start_time', 'end_time', 'event_type', 'event_details', 'event_description']

    event_type = forms.ChoiceField(choices=[
        ('marriage', 'Marriage'),
        ('meeting', 'Meeting'),
        ('baptism', 'Baptism'),
        ('others', 'Others'),
    ])
