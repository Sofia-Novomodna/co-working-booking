from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .serializers import UserRegistrationSerializer

from django.utils import timezone
from datetime import datetime
from .models import Room, Booking

# Create your views here.
from django.shortcuts import render, redirect
from .forms import RegistrationForm, BookingForm


def register_view(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # This saves the user to the database
            form.save() 
            return redirect('login') # Redirect after successful save
    else:
        form = RegistrationForm()
        
    return render(request, 'main/register.html', {'form': form})



@login_required
def dashboard_view(request):
    return render(request, 'main/dashboard.html')

@login_required
def home_view(request):
    return render(request, 'main/home.html')

@login_required
def map_view(request):
    return render(request, 'main/map.html')

@login_required
def tab1(request):
    return render(request, 'main/tab1.html')
@login_required
def tab2(request):
    return render(request, 'main/tab2.html')
@login_required
def tab3(request):
    return render(request, 'main/tab3.html')


from django.db import transaction

@login_required
def booking_view(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            room = form.cleaned_data["room"]
            start_time = form.cleaned_data["start_time"]
            end_time = form.cleaned_data["end_time"]

            with transaction.atomic():
                # Lock the room row until this transaction commits
                Room.objects.select_for_update().get(pk=room.pk)

                conflict_exists = Booking.objects.filter(
                    room=room,
                    booked_by__isnull=False,
                    start_time__lt=end_time,
                    end_time__gt=start_time,
                ).exists()

                if conflict_exists:
                    form.add_error(
                        None,
                        "This room was just booked by someone else for that time.",
                    )
                else:
                    booking = form.save(commit=False)
                    booking.booked_by = request.user
                    booking.save()
                    return redirect("home")
    else:
        form = BookingForm()

    return render(request, "main/booking.html", {"form": form})






from django.shortcuts import render
from .models import Booking
import django_tables2 as tables

class BookingTable(tables.Table):
    class Meta:
        model = Booking
        template_name = "django_tables2/bootstrap.html"
        fields = ("room", "booked_by", "start_time", "end_time")
        exclude = ["booked_by"]


class TableView(tables.SingleTableView):
    table_class = BookingTable
    template_name = "main/table_bookings.html"
    paginate_by = 5

    def get_queryset(self):
        return Booking.objects.exclude(
            room__room_name="Desks",
            room__room_class="Hot Desks",
        )
        





#class TableView(tables.SingleTableView):
    #table_class = BookingTable
    #queryset = Booking.objects.all()
    #template_name = "main/table_bookings.html"
    #paginate_by = 10  # Show 10 records per page

    #def get_queryset(self):
        #return Booking.objects.exclude(room__room_name__icontains="Hot Desks")









#class UserRegistrationView(APIView):
    #def post(self, request):
        #serializer = UserRegistrationSerializer(data=request.data)
        #if serializer.is_valid():
            #serializer.save()
            #return Response({
              #"message": "User registered successfully"
            #}, status=status.HTTP_201_CREATED)
        #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

#class UserRegistrationView(generics.CreateAPIView):
    #serializer_class = UserRegistrationSerializer

