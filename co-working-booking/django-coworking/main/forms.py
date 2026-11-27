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

        

from django.core.exceptions import ValidationError
from datetime import timedelta

class BookingForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Booking
        fields = ["room", "start_time", "end_time"]
        widgets = {
            'start_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        room = cleaned_data.get("room")
        start_time = cleaned_data.get("start_time")
        end_time = cleaned_data.get("end_time")

        if not room or not start_time or not end_time:
            raise ValidationError("Room, start time, and end time are required.")

        if end_time - start_time < timedelta(hours=1):
            raise ValidationError("Booking must be at least 1 hour long")

        overlapping = Booking.objects.filter(
            room=room,
            booked_by__isnull=False,  # ignore unassigned placeholder rows if you use them
            start_time__lt=end_time,
            end_time__gt=start_time,
        )

        # Exclude current instance if editing an existing booking
        if self.instance and self.instance.pk:
            overlapping = overlapping.exclude(pk=self.instance.pk)

        if overlapping.exists():
            raise ValidationError(
                "This room is already booked during the selected time range."
            )

        return cleaned_data


