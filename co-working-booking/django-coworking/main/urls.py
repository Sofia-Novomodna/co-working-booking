from django.urls import path
#from django.contrib.auth.views import LoginView, LogoutView
from .views import register_view, dashboard_view, home_view, booking_view



urlpatterns = [
    path('register/', register_view, name='register'),
    #path('login/', LoginView.as_view(template_name='main/login.html'), name='login'),
    #path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('home/', home_view, name='home'),
    path('booking/', booking_view, name='booking'),
]