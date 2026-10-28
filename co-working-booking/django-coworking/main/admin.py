from django.contrib import admin

# Register your models here.
from .models import Room, Booking

# Register your models here once
admin.site.register(Room)
admin.site.register(Booking)