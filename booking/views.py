from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import TravelOption, Booking
from .forms import SignUpForm, BookingForm, UserUpdateForm
from django.utils import timezone

@login_required
def booking_list(request):
	bookings = Booking.objects.filter(user=request.user).order_by('-date')
	return render(request, 'booking/booking_list.html', {'bookings': bookings})

@login_required
def cancel_booking(request, pk):
	booking = get_object_or_404(Booking, pk=pk, user=request.user)
	if booking.status != 'cancelled':
		booking.status = 'cancelled'
		booking.save()
		# Restore seats
		travel_option = booking.travel_option
		travel_option.seats += booking.seats
		travel_option.save()
	return redirect('booking_list')

def signup(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			return redirect('travel_option_list')
	else:
		form = SignUpForm()
	return render(request, 'registration/signup.html', {'form': form})

@login_required
def profile(request):
	if request.method == 'POST':
		form = UserUpdateForm(request.POST, instance=request.user)
		if form.is_valid():
			form.save()
			return redirect('profile')
	else:
		form = UserUpdateForm(instance=request.user)
	return render(request, 'registration/profile.html', {'form': form})

def travel_option_list(request):
	options = TravelOption.objects.all()
	type_filter = request.GET.get('type')
	source_filter = request.GET.get('source')
	destination_filter = request.GET.get('destination')
	date_filter = request.GET.get('date')
	if type_filter:
		options = options.filter(type=type_filter)
	if source_filter:
		options = options.filter(source__icontains=source_filter)
	if destination_filter:
		options = options.filter(destination__icontains=destination_filter)
	if date_filter:
		options = options.filter(departure__date=date_filter)
	return render(request, 'booking/travel_option_list.html', {'options': options})

@login_required
def booking_form(request, pk):
	option = get_object_or_404(TravelOption, pk=pk)
	from django.utils import timezone
	if request.method == 'POST':
		form = BookingForm(request.POST)
		if form.is_valid():
			seats_requested = form.cleaned_data['seats']
			now = timezone.now()
			if option.departure < now:
				form.add_error(None, 'Cannot book travel options with a past departure date.')
			elif seats_requested > option.seats:
				form.add_error('seats', 'Not enough seats available.')
			else:
				booking = form.save(commit=False)
				booking.user = request.user
				booking.travel_option = option
				booking.price = option.price * booking.seats
				booking.save()
				option.seats -= seats_requested
				option.save()
				return redirect('booking_list')
	else:
		form = BookingForm()
	return render(request, 'booking/booking_form.html', {'form': form, 'option': option})

# Create your views here.
