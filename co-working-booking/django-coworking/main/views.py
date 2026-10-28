from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .serializers import UserRegistrationSerializer

from django.utils import timezone
from datetime import datetime
from .models import Room, Booking

# Create your views here.



def register_view(request):
    errors = {}
    if request.method == 'POST':
        serializer = UserRegistrationSerializer(data=request.POST)
        if serializer.is_valid():
            user = serializer.save()
            login(request, user)  # Automatically log them in
            messages.success(request, "Registration successful! Welcome.")
            return redirect('dashboard')
        else:
            errors = serializer.errors

    return render(request, 'main/register.html', {'errors': errors})

@login_required
def dashboard_view(request):
    return render(request, 'main/dashboard.html')

@login_required
def home_view(request):
    return render(request, 'main/home.html')


@login_required
def booking_view(request):
    errors = {}
    # Fetch all rooms from DB
    rooms = Room.objects.all()

    if request.method == "POST":
        room_id = request.POST.get("room")
        start_time_str = request.POST.get("start_time")
        end_time_str = request.POST.get("end_time")

        if not room_id:
            errors["room"] = ["Please select a room."]
        if not start_time_str:
            errors["start_time"] = ["Start time is required."]
        if not end_time_str:
            errors["end_time"] = ["End time is required."]

        if not errors:
            try:
                start_time = timezone.make_aware(datetime.strptime(start_time_str, "%Y-%m-%dT%H:%M"))
                end_time = timezone.make_aware(datetime.strptime(end_time_str, "%Y-%m-%dT%H:%M"))

                if end_time <= start_time:
                    errors["end_time"] = ["End time must be after start time."]
                else:
                    selected_room = Room.objects.get(id=room_id)

                    # Save record to Booking table
                    booking = Booking(
                        room=selected_room,
                        booked_by=request.user,
                        start_time=start_time,
                        end_time=end_time
                    )
                    booking.save()

                    messages.success(request, "Booking confirmed successfully!")
                    return redirect("home")

            except Room.DoesNotExist:
                errors["room"] = ["Selected room does not exist."]
            except ValueError:
                errors["start_time"] = ["Invalid date/time format."]

    # ALWAYS pass rooms in context
    context = {
        "rooms": rooms,
        "errors": errors,
    }
    return render(request, "main/booking.html", context)





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

