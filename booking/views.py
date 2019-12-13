from django.shortcuts import render
from .models import *
from rest_framework import viewsets
from .serializer import ConcertSerializer


class ConcertSet(viewsets.ModelViewSet):
	queryset = Concert.objects.all().order_by('id')
	serializer_class = ConcertSerializer

def show_index(request):
	singer_list = Concert.objects.all()
	context = {
	'singer_list' : singer_list,
	}
	return render (request, 'common/booking.html',context)