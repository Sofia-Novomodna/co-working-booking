from django.urls import path
#from django.contrib.auth.views import LoginView, LogoutView
from .views import register_view, dashboard_view, home_view, booking_view, map_view, tab1, tab2, tab3, TableView, MyBookingsView



urlpatterns = [
    path('register/', register_view, name='register'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('home/', home_view, name='home'),
    path('booking/', booking_view, name='booking'),
    path('map/', map_view, name='map'),
    path('tab1/', tab1, name='tab1'),
    path('tab2/', tab2, name='tab2'),
    path('tab3/', tab3, name='tab3'),
    path('table/', TableView.as_view(), name='table'),
    path('mybookings/', MyBookingsView.as_view(), name='mybookings'),
]