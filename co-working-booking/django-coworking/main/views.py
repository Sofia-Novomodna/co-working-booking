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



@login_required
def booking_view(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            # This saves the user to the database
            # 1. Create the booking object, but don't save to DB yet
            booking = form.save(commit=False)
            # 2. Automatically assign the logged-in user
            booking.booked_by = request.user
            # 3. Now save it to the database
            booking.save()
            return redirect('home') # Redirect after successful save
    else:
        form = BookingForm()
        
    return render(request, "main/booking.html", {'form': form})











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

