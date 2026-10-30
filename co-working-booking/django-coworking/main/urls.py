from django.urls import path
#from django.contrib.auth.views import LoginView, LogoutView
from .views import register_view, dashboard_view, home_view, booking_view



urlpatterns = [
    path('register/', register_view, name='register'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('home/', home_view, name='home'),
    path('booking/', booking_view, name='booking'),
]