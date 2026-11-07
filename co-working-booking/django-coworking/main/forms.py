# import form class from django
from django import forms
 
# import GeeksModel from models.py
from .models import User, Booking
 
# create a ModelForm
class RegistrationForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = User
        fields = ["username", "password"]

        
class BookingForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Booking
        fields = ["room", "start_time", "end_time"]
        widgets = {
            'start_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }


