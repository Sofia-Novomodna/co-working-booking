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




 <form method="POST">
                {% csrf_token %}
                
                <!-- Username -->
                <div class="mb-3">
                    <label class="form-label">Username</label>
                    <input type="text" name="username" class="form-control" value="{{ request.POST.username|default:'' }}" required>
                    {% if errors.username %}
                        <div class="text-danger small mt-1">{{ errors.username.0 }}</div>
                    {% endif %}
                </div>

                <!-- Email -->
                <div class="mb-3">
                    <label class="form-label">Email address</label>
                    <input type="email" name="email" class="form-control" value="{{ request.POST.email|default:'' }}" required>
                    {% if errors.email %}
                        <div class="text-danger small mt-1">{{ errors.email.0 }}</div>
                    {% endif %}
                </div>

                <!-- Password -->
                <div class="mb-3">
                    <label class="form-label">Password</label>
                    <input type="password" name="password" class="form-control" required>
                    {% if errors.password %}
                        <div class="text-danger small mt-1">{{ errors.password.0 }}</div>
                    {% endif %}
                </div>

                <!-- Confirm Password (password2) -->
                <div class="mb-3">
                    <label class="form-label">Confirm Password</label>
                    <input type="password" name="password2" class="form-control" required>
                </div>

                <button type="submit" class="btn btn-primary w-100 py-2 mt-2">Register</button>
            </form>
            
            <div class="text-center mt-3">
                <small class="text-muted">Already have an account? <a href="{% url 'login' %}">Login here</a></small>
            </div>













 <div class="row justify-content-center mt-3">
        C
            
            <div class="card p-4 shadow-sm border border-2 border-warning border-opacity-50 rounded-4" style="background-color: rgba(253, 248, 238, 0.95); border-color: #D9C3A1 !important;">
                
                <h2 class="text-center mb-4 fw-bold" style="color: #3D2314;">New Booking</h2>
                
                <form method="POST">
                    {% csrf_token %}
                    <!-- Room Selection -->

<div class="mb-3">
    <label class="form-label fw-bold text-uppercase small text-secondary">Select Room / Area</label>
    <select name="room" class="form-select bg-light shadow-none" required>
        <option value="" disabled selected>Choose a space...</option>
        {% for room in rooms %}
            <option value="{{ room.id }}">{{ room.room_name }}</option>
        #{% empty %}
            #<option value="" disabled>No rooms available in database</option>
        #{% endfor %}
    </select>
    {% if errors.room %}
        <div class="text-danger small mt-1">{{ errors.room.0 }}</div>
    {% endif %}
</div>

                    <!-- Start Time -->
                    <div class="mb-3">
                        <label class="form-label fw-bold text-uppercase small text-secondary">Start Time</label>
                        <input type="datetime-local" name="start_time" class="form-control bg-light shadow-none" value="{{ request.POST.start_time|default:'' }}" required>
                        {% if errors.start_time %}
                            <div class="text-danger small mt-1">{{ errors.start_time.0 }}</div>
                        {% endif %}
                    </div>

                    <!-- End Time -->
                    <div class="mb-3">
                        <label class="form-label fw-bold text-uppercase small text-secondary">End Time</label>
                        <input type="datetime-local" name="end_time" class="form-control bg-light shadow-none" value="{{ request.POST.end_time|default:'' }}" required>
                        {% if errors.end_time %}
                            <div class="text-danger small mt-1">{{ errors.end_time.0 }}</div>
                        {% endif %}
                    </div>

                    <button type="submit" class="btn w-100 py-2 mt-2 fw-semibold text-white shadow-sm" style="background-color: #D68C13; border-color: #D68C13;">Confirm Booking</button>
                </form>
                
                <div class="text-center mt-3">
                    <small class="text-muted"><a href="{% url 'home' %}" class="text-decoration-none" style="color: #6B4C3B;">Back to Home</a></small>
                </div>

            </div>

        </div>
    </div>





