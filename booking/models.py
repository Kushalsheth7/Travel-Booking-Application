from django.db import models
from django.contrib.auth.models import User

class TravelOption(models.Model):
	TYPE_CHOICES = [
		('flight', 'Flight'),
		('train', 'Train'),
		('bus', 'Bus'),
	]
	type = models.CharField(max_length=10, choices=TYPE_CHOICES)
	source = models.CharField(max_length=100)
	destination = models.CharField(max_length=100)
	departure = models.DateTimeField()
	price = models.DecimalField(max_digits=8, decimal_places=2)
	seats = models.PositiveIntegerField()

	def __str__(self):
		return f"{self.type.title()} from {self.source} to {self.destination}"

class Booking(models.Model):
	STATUS_CHOICES = [
		('booked', 'Booked'),
		('cancelled', 'Cancelled'),
	]
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	travel_option = models.ForeignKey(TravelOption, on_delete=models.CASCADE)
	seats = models.PositiveIntegerField()
	price = models.DecimalField(max_digits=8, decimal_places=2)
	date = models.DateTimeField(auto_now_add=True)
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='booked')

	def __str__(self):
		return f"Booking {self.id} by {self.user.username}"

# Create your models here.
