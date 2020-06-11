from django.shortcuts import render

from django.http import HttpResponse


# Create your views here.
def index(request):
	# Construct a dictionary to pass to the template engine as its context.
	# Note the key boldmessage matches to {{ boldmessage }} in the template!
	context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}

	# Return a rendered response to send to the client.
	# We make use of the shortcut function to make our lives easier.
	# Note that the first parameter is the template we wish to use.
	#request.session.set_test_cookie()
	#return render(request, 'rango/index.html', context=context_dict)
	return HttpResponse("Rango says hey there partner! <br> <a href='/rango/about/'>About</a>")


def about(request):
	'''
	if request.session.test_cookie_worked():
		print("TEST COOKIE WORKED!")
		request.session.delete_test_cookie()
	'''
	return HttpResponse("Rango says here is the about page. <br> <a href='/rango/'>Index</a>")

'''
def visitor_cookie_handler(request, response):
	# Get the number of visits to the side.
	# We use the COOKIES.get() function to obtain the visits cookie.
	# If the cookie exists, the value returned is cased to an integer.
	# If the cookie doesn't exist, then the default value of 1 is used.
	visits = int(request.COOKIES.get('visits', '1'))

	last_visit_cookie = request.COOKIES.get('last_visit', str(datetime.now()))
	last_visit_time = datetime.strptime(last_visit_cookie[:-7], '%Y-%m-%d %H:%M:%S')

	# If it's been more than a day since the last visit...
	if (datetime.now() - last_visit_time).days > 0:
		visits = visits + 1
		# Update the last visit cookie now that we have updated the count
		response.set_cookie('last_visit', str(datetime.now()))
	else:
		# Set the last visit cookie
		response.set_cookie('last_visit', last_visit_cookie)

	# Update/set the visits cookie
	response.set_cookie('visits', visits)
'''