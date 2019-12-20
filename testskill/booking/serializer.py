from rest_framework import serializers
from .models import *

class ConcertSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Concert
		fields = ('singer','image','city','address','date','time','trailer',)