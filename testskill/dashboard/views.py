from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.

def home (request):
	context={}
	return render (request,'home.html',context)
	
def about(request):
	"""about page"""
	context = {}
	template = 'about.html'
	return render(request,template,context)

@login_required
def dashboard(request):
	context={'user':request.user}
	return render (request,'dashboard.html',context)