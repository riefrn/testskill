from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import *
from rest_framework import viewsets
from .serializer import ConcertSerializer
from django.core.mail import send_mail
from . import views
from .forms import SeatForm, BookingForm, SelectedSeatForm
import datetime


class ConcertSet(viewsets.ModelViewSet):
	queryset = Concert.objects.all().order_by('id')
	serializer_class = ConcertSerializer

@login_required
def reserve_seat (request, concert_id):
	try :
		show_info = Concert.objects.get(pk=concert_id)
	except Concert.DoesNotExist:
		raise Http404 ("Page Dose Not Exist.")
	form = SeatForm()
	form2 = SelectedSeatForm()
	context = {'show_info' : show_info,
				'form':form,
				'form2':form2,
			}

	return render (request,'booking/reserve_seat.html',context)

@login_required
def payment_gateway(request):
	if request.POST:
		seats = request.POST.get('selected_seat')
		seat_type = request.POST.get('seat_type')
		concert_id = request.POST.get('concert_id')

		concert = Concert.objects.get(pk=concert_id)
		seats = seats.split(',')
		book_seat = []
		for each in seats:
			try:
                #if seat not found in DB
				s = Seat.objects.get(seat_type=seat_type, no=each, show=concert)
			except:
                #redirect to seatnotfound.html
				return redirect('booking/seatnotfound.html')

			if Seat.objects.filter(seat_type=seat_type, no=each, show=concert):
				s = Seat(no=each, seat_type=seat_type, show=concert)
				book_seat.append(s)

		form = BookingForm()

		price_rate = 100000 #Yes.
		ticket_price = price_rate * len(book_seat)

        #Creating the seat string.
		seat_str = ""
		for i in range(len(seats)):
			if i == len(seats)-1:
				seat_str += seats[i]
			else:
				seat_str += seats[i] + ','
		context = {
				'seats':seat_str,
				'seat_type':seat_type,
				'concert':concert,
				'form':form,
				'ticket_price':ticket_price,
			}
		return render (request,'booking/payment_gateway.html', context)
	else :
		return redirect('home')	

def payment_confirmation(request):
	if request.POST:
		concert_id = request.POST.get('concert_id')
		concert = Concert.objects.get(pk=concert_id)
		seats = request.POST.get('selected_seat')
		seats = seats.split(',')
		seat_type = request.POST.get('seat_type')
		timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		payment_type = request.POST.get('payment_type')
		paid_amount = request.POST.get('amount')
		paid_by = request.user
		id = str(concert)+str(seats)+timestamp
		book = Booking(id=id, timestamp=timestamp, payment_type=payment_type, paid_amount=paid_amount,paid_by=paid_by)
		book.save()

		booked_seat = []

		for seat in seats:
			print (seat)
			s = Seat.objects.get(no=seat, show=concert)
			b = Booking.objects.get(pk=id)
			try:
				sc = BookedSeat.objcts.get(seat=s)
			except:
				booked = BookedSeat(seat=s, booking=b)
				booked_seat.append(booked)
			else:
				return redirect('booking/seatconflict.html')
		BookedSeat.objects.bulk_create(booked_seat)
		return render(request, 'booking/payment_confirmation.html')

def concert_list(request, concert_id):
	concert_list = Concert.objects.get(id=concert_id)
	context ={
		'concert_list' : concert_list
	}
	return render (request,'concert/concert_list.html', context)

def show_index(request):
	singer_list = Concert.objects.all()
	context = {
	'singer_list' : singer_list,
	}
	return render (request, 'common/booking.html',context)