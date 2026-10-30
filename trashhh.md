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