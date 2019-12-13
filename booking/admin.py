from django.contrib import admin

from .models import Concert

class ConcertAdmin(admin.ModelAdmin):
	class Meta:
		model = Concert
admin.site.register(Concert,ConcertAdmin)