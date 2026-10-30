from django.db import models
import datetime
from django.utils import timezone
# Create your models here.


from django.contrib.auth.models import User

class RoomClass(models.TextChoices):
        DESKS = "Hot Desks", "Hot Desks"
        OFFICES = "Private Offices", "Private Offices"
        TEAM = "Team Suites", "Team Suites"
        MEETING = "Meeting and Conference Rooms", "Meeting and Conference Rooms"
        LOUNGE = "Lounge and Cafe Areas", "Lounge and Cafe Areas"
class Room(models.Model):


    room_name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    
    room_class = models.CharField(
        max_length=50,  # shortened max_length to fit choices safely
        choices=RoomClass.choices,
        default=RoomClass.DESKS,
    )

    def __str__(self):
        return f"{self.room_name} ({self.get_room_class_display()})"


class Booking(models.Model):
    # Link the booking to a specific room
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="bookings")
    booked_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)

    @property
    def is_active(self):
        """Returns True if the booking has a user assigned."""
        return self.booked_by is not None

    def __str__(self):
        if self.booked_by:
            return f"{self.room.room_name} - Booked by {self.booked_by.username}"
        return f"{self.room.room_name} - Available / Unassigned"