from django.contrib import admin

from .models import Concert, Seat, BookedSeat, Booking

class ConcertAdmin(admin.ModelAdmin):
	class Meta:
		model = Concert
admin.site.register(Concert,ConcertAdmin)

class SeatAdmin(admin.ModelAdmin):
	class Meta:
		model = Seat
admin.site.register(Seat,SeatAdmin)

class BookedSeatAdmin(admin.ModelAdmin):
	class Meta:
		model = BookedSeat

class BookingAdmin(admin.ModelAdmin):
	class Meta:
		model = Booking

admin.site.register(Booking,BookingAdmin)
