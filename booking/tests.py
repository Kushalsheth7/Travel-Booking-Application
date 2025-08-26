from django.test import TestCase
from django.contrib.auth.models import User
from .models import TravelOption, Booking

class UserTestCase(TestCase):
	def test_user_registration(self):
		user = User.objects.create_user(username='testuser', email='test@example.com', password='testpass123')
		self.assertEqual(user.username, 'testuser')
		self.assertEqual(user.email, 'test@example.com')

class BookingTestCase(TestCase):
	def setUp(self):
		self.user = User.objects.create_user(username='booker', password='pass123')
		self.option = TravelOption.objects.create(type='flight', source='A', destination='B', departure='2025-08-26T10:00', price=1000, seats=10)

	def test_booking_creation(self):
		booking = Booking.objects.create(user=self.user, travel_option=self.option, seats=2, price=2000)
		self.assertEqual(booking.user.username, 'booker')
		self.assertEqual(booking.seats, 2)
		self.assertEqual(booking.price, 2000)

# Create your tests here.
