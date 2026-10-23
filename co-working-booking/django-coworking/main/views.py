from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .serializers import UserRegistrationSerializer

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
    return render(request, 'main/booking.html')


@login_required
def booking_view(request):
    if request.method == 'POST':
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')
        
        # Save the booking and assign the current logged-in user automatically
        Booking.objects.create(
            booked_by=request.user,
            start_time=start_time,
            end_time=end_time
        )
        return redirect('home') # Redirect to home or bookings list after success
        
    return render(request, 'main/booking.html')

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

