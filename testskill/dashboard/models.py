from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from allauth.account.signals import user_logged_in, user_signed_up
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY

class dashboard (models.Model):
	username = models.CharField(max_length = 100 )
	user = models.OneToOneField(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE)
	about = models.TextField(default = 'default about text')
	location = models.CharField(default="location defualt text", max_length=200, blank=True)
	worktitle = models.CharField(max_length=100, null=True, blank=True)
	def __unicode__(self):
		return self.username

class stripeUser(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	stripe_id = models.CharField(max_length=200, null=True, blank=True)

	def __unicode__(self):
		if self.stripe_id:
			return str(self.stripe_id)
		else :
			return self.user.username

def stripeCallback(sender, request,user, **kwargs):
	user_stripe_account,create=stripeUser.objects.get_or_create(user=user)
	if create:
		print ('create for %s'%(user.username))
	if user_stripe_account.stripe_id is None or user_stripe_account.stripe_id=='':
		new_stripe_id = stripe.Customer.create(email=user.email)
		user_stripe_account.stripe_id = new_stripe_id['id']
		user_stripe_account.save()

def dashboardCallback(sender, request, user, **kwargs):
	userdashboard, is_created = dashboard.objects.get_or_create(user=user)
	if is_created:
		userdashboard.username = user.username
		userdashboard.save()

user_logged_in.connect(stripeCallback)
user_signed_up.connect(dashboardCallback)
user_signed_up.connect(stripeCallback)