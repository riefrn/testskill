from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework import routers

from dashboard import views as dash_views
from booking import views as booking_views
from contact import views as cont_views

router = routers.DefaultRouter()
router.register(r'concerts',booking_views.ConcertSet, base_name="booking_concert")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',dash_views.home, name='home'),
    path('contact/',cont_views.contact, name='contact'),
    path('accounts/', include('allauth.urls')),
    path('booking/',booking_views.show_index, name='booking'),
    path('api/',include(router.urls),name='api'),
    path('api-auth/',include('rest_framework.urls', namespace='rest_framework')),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) #all values set in settings.py
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
