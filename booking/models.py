from __future__ import unicode_literals
from django.db import models
from django.conf import settings
from allauth.account.signals import user_logged_in, user_signed_up

import datetime

class Concert(models.Model):
	city_choice=(
		('JAKARTA','Jakarta'),
		('BANDUNG','Bandung'),
		('SURABAYA','Surabaya'),
		('SEMARANG','Semarang'),
		('MEDAN','Medan'),
		)
	singer 		= models.CharField(max_length= 50, null=True, blank=True)
	image		= models.ImageField(null=True, blank=True, upload_to='media')
	city 		= models.CharField(max_length=8, choices=city_choice, null=False)
	address		= models.CharField(max_length=200)
	date 		= models.DateField()
	time 		= models.TimeField()
	trailer		= models.URLField(blank=True)
	def __str__ (self):
		return str(self.singer)+ "-" +str(self.city) +"-"+str(self.date)+"-"+str(self.time)

class Booking(models.Model):
	payment_choice = (
		('Credit Card' , 'Credit Card'),
		)
	id = models.CharField(primary_key=True, max_length=200)
	timestamp = models.DateTimeField('%Y-%m-%d %H:%M:%S', null=True, blank=True)
	payment_type = models.CharField(max_length=11, choices=payment_choice, default='Credit Card')
	paid_amount =  models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
	paid_by	= models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.DO_NOTHING, null=True, blank=True)

class Seat (models.Model):
	seat_choice = (
		('','Select'),
		('Silver','Silver'),
		('Gold','Gold'),
		('Platinum','Platinum'),
		)
	no = models.CharField(max_length=3, null=True, blank=False)
	seat_type = models.CharField(max_length=8, choices=seat_choice, blank=False)
	show = models.ForeignKey(Concert, on_delete=models.CASCADE)
	class Meta:
		unique_together = ('no', 'show')

	def __str__(self):
		return self.no +str(self.show)

class BookedSeat(models.Model):
	seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
	booking=models.ForeignKey(Booking, on_delete=models.CASCADE)

	class Meta :
		unique_together = ('seat', 'booking')
	def __str__(self):
		return str(self.seat) + '|' + str(self.booking)