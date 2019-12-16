from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include, re_path
from rest_framework import routers
from django.views.generic import TemplateView


from dashboard import views as dash_views
from booking import views as booking_views
from contact import views as cont_views
from checkout import views as check_views
router = routers.DefaultRouter()
router.register(r'concerts',booking_views.ConcertSet, base_name="booking_concert")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',dash_views.home, name='home'),
    path('contact/',cont_views.contact, name='contact'),
    path('accounts/', include('allauth.urls')),
    path('booking/',booking_views.show_index, name='booking'),
    path('checkout/',check_views.checkout, name='checkout' ),
    path('api/',include(router.urls),name='api'),
    path('api-auth/',include('rest_framework.urls', namespace='rest_framework')),
    re_path (r'^booking/(?P<concert_id>\d+)/$', booking_views.concert_list, name='concert_list'),
    re_path(r'^booking/seatchoice/(?P<concert_id>\d+)/$', booking_views.reserve_seat, name='reserve_seat'),
    path('booking/payment/', booking_views.payment_gateway, name='payment_gateway'),
    path('booking/payment_confirmation/', booking_views.payment_confirmation, name='payment_confirmation'),
    #Hard Coded templates i.e. without views.
    path('booking/payment/booking/seatnotfound.html', TemplateView.as_view(template_name="booking/seatnotfound.html"), name='seatnotfound'),
    path('booking/payment_confirmation/booking/seatconflict.html', TemplateView.as_view(template_name="booking/seatconflict.html"), name='seatconflict'),

]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) #all values set in settings.py
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
