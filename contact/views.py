from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

from .forms import contactForm
from . import autoreply

def contact(request):
	title= "Contact"
	form = contactForm(request.POST or None)
	confirmation=None

	if form.is_valid():
		user_name = form.cleaned_data['Username']
		user_message = form.cleaned_data['Message']
		emailsub = user_name + " tried contacting you on Concert"
		emailFrom = form.cleaned_data ['UserEmail']
		emailmessage = '%s %s user email: %s' %(user_message, user_name, emailFrom)
		emailTo = [settings.EMAIL_HOST_USER]
		send_mail(emailsub, emailmessage, emailFrom, list(emailTo), fail_silently=True)
		#Autoreply.
		autoreply.autoreply(emailFrom)
		title = "Thanks."
		confirmation = "We will get right back to you."
		form = None
		
	context = {
		'title':title, 
		'form':form, 
		'confirmation':confirmation,
		}
	return render (request,'contact/contact.html',context)
	