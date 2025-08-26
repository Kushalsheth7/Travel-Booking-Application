from django.core.management.base import BaseCommand
from booking.models import TravelOption
from django.utils import timezone
from datetime import timedelta

class Command(BaseCommand):
    help = 'Create mock travel options for testing'

    def handle(self, *args, **kwargs):
        TravelOption.objects.all().delete()
        now = timezone.now()
        options = [
            TravelOption(type='flight', source='Mumbai', destination='Delhi', departure=now+timedelta(days=1), price=3500, seats=50),
            TravelOption(type='train', source='Delhi', destination='Agra', departure=now+timedelta(days=2), price=800, seats=100),
            TravelOption(type='bus', source='Agra', destination='Jaipur', departure=now+timedelta(days=3), price=500, seats=40),
            TravelOption(type='flight', source='Bangalore', destination='Goa', departure=now+timedelta(days=4), price=2500, seats=60),
            TravelOption(type='train', source='Chennai', destination='Hyderabad', departure=now+timedelta(days=5), price=1200, seats=80),
        ]
        TravelOption.objects.bulk_create(options)
        self.stdout.write(self.style.SUCCESS('Mock travel options created.'))
