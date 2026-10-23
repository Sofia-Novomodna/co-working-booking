from django.db import models
import datetime
from django.utils import timezone
# Create your models here.


from django.contrib.auth.models import User


class Room(models.Model):
    class RoomClass(models.TextChoices):
            DESKS = 'Hot Desks'
            OFFICES = 'Private Offices'
            TEAM = 'Team Suites'
            MEETING = 'Meeting and Conference Rooms'
            LOUNGE = 'Lounge and Cafe Areas'


    room_name = models.CharField(max_length=100)
    booked_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    
    # Class chosen from the proposed list
    room_class = models.CharField(
        max_length=100,
        choices=RoomClass.choices,
        default=RoomClass.DESKS,
    )
    
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    


    @property
    def is_free(self):
        """Returns True if the room has no user booked to it."""
        return self.booked_by is None

    def __str__(self):
        if self.booked_by:
            return f"{self.room_name} - Booked by {self.booked_by.username}"
        return f"{self.room_name} - FREE"