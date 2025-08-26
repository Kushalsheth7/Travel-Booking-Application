from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('', views.travel_option_list, name='travel_option_list'),
    path('book/<int:pk>/', views.booking_form, name='booking_form'),
    path('bookings/', views.booking_list, name='booking_list'),
    path('cancel/<int:pk>/', views.cancel_booking, name='cancel_booking'),
]
