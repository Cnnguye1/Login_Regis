from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
# Create your views here.
from .models import *
def index(request):

	# return HttpResponse('got here')
	# return render(request, 'registration/index.html')

	if request.method == 'POST':
		errors = Registration.objects.validate(request.POST)
		if len(errors):
			for tag, error in errors.iteritems():
				messages.error(request, error, extra_tags=tag)
			# return render(request, 'registration/index.html')
			return redirect('/registration')
		else:
			Registration.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=request.POST['password'])
			messages.success(request, 'Registration is successful! Please, Log in!')
			return redirect('/registration')
	else:
		return render(request, 'registration/index.html')

			

def login(request):
	print len(Registration.objects.filter(email = request.POST['email']))
	if request.method == 'POST':
		if len(Registration.objects.filter(email = request.POST['email'])) > 0 and len(Registration.objects.filter(password = request.POST['password'])) > 0:
			context = {
				'user': Registration.objects.get(email = request.POST['email'])
			}
			return render(request, 'registration/success.html', context)
		else:
			messages.error(request, 'Check your Log In or Register First!')
			return redirect('/registration')
	else:
		redirect('/registration')
	# if request.method == "POST":
	# 	email = request.POST['email']
	# 	if len(Registration.objects.filter(email = email)) >1:
	# 		print str(email)
	# 		context = {
	# 			'user': Registration.objects.get(email = email)
	# 		}
	# 		return render(request, 'registration/success.html', context)
	# 	else:
	# 		messages.error(request, 'Check your Log In or Register First!')
	# 		return redirect('/registration')
