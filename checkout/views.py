from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.conf import settings
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY

# Create your views here.

@login_required
def checkout(request):
	publishkey = settings.STRIPE_PUBLISHABLE_KEY
	customer_id = request.user.stripeuser.stripe_id
	if request.method == 'POST':
		token = request.POST.get('stripeToken')
		try:
			customer = stripe.Customer.create( source=token)
			# customer.sources.create(source=token)

			charge = stripe.Charge.create(
				amount=100000,
				currency="usd",
				description = "Example charge",
				customer = customer_id,
				)
		except stripe.error.CardError as e:
				print ('The Card has been decline')
				pass
	context = {
			'publishKey':publishkey
			}
	return render (request, 'checkout.html', context)