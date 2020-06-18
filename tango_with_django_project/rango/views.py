from django.shortcuts import render

from django.http import HttpResponse

# Import the Category model
from rango.models import Category
from rango.models import Page


# Create your views here.
def index(request):
	# Query the database for a list of ALL categories currently stored.
	# Order the categories by the number of likes in descending order.
	# Retrieve the top 5 only -- or all if less than 5
	# Place the list in our context_dict dictionary (with our boldmessage!)
	# that will be passed to the template engine.
	category_list = Category.objects.order_by('-likes')[:5]
	page_list = Page.objects.order_by('-views')[:5]


	# Construct a dictionary to pass to the template engine as its context.
	# Note the key boldmessage matches to {{ boldmessage }} in the template!
	context_dict = {}
	context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
	context_dict['categories'] = category_list
	context_dict['pages'] = page_list

	# Return a rendered response to send to the client.
	# We make use of the shortcut function to make our lives easier.
	# Note that the first parameter is the template we wish to use.
	#request.session.set_test_cookie()
	return render(request, 'rango/index.html', context=context_dict) # chp-4
	#return HttpResponse("Rango says hey there partner! <br> <a href='/rango/about/'>About</a>")


def about(request):
	'''
	if request.session.test_cookie_worked():
		print("TEST COOKIE WORKED!")
		request.session.delete_test_cookie()
	'''
	context_msg = {'boldmessage': "here is the about page."}

	#return HttpResponse("Rango says here is the about page. <br> <a href='/rango/'>about</a>") # chp-3
	return render(request, 'rango/about.html', context=context_msg)


def show_category(request, category_name_slug):
	# Create a context dictionary which we can pass to the templage rendering engine.
	context_dict = {}

	try:
		# Can we find a category name slug with the given name?
		# If we can't, the .get() method raises a DoesNotExist exception.
		# The .get() method returns one model instance or raises and exception.
		category = Category.objects.get(slug=category_name_slug)

		# Retrieve all of the associated pages.
		# The filter() will return a list of page objects or an empty list.
		pages = Page.objects.filter(category=category)

		# Adds our results list to the template context under name pages.
		context_dict['pages'] = pages
		# We also add the category object from the database to the context dictionary.
		# We'll use this in the template to verify that the category exists.
		context_dict['category'] = category
	except Category.DoesNotExist:
		# We get here if we didn't find the specified category.
		# Don't do anything - 
		# the template will display the "no category" message for us.
		context_dict['category'] = None
		context_dict['pages'] = None

	# Go render the response and return it to the client.
	return render(request, 'rango/category.html', context=context_dict)

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

