from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, get_user_model

from .forms import ContactForm, LoginForm, RegisterForm


def home_page(request):
	context = {
	"title": "Home Page",
	"content": "This is home page",
	}
	print(context)
	if request.user.is_authenticated():
		context["premium_content"] = "YEAHHHH"
		print(context)
		print(request.user.is_authenticated())
		print(request.user.is_authenticated)
		print(request.user)
		print(request)
	return render(request, 'home_page.html', context)


def about_page(request):
	context = {
	"title": "About Page",
	"content": "This is about page"
	}
	return render(request, 'home_page.html', context)

def contact_page(request):

	###my part
	# contact_form = ContactForm(request.POST)
	# print('---type contact_form = ContactForm(request.POST)')
	# print(type(contact_form))
	# print('---print contact_form')
	# print(contact_form)#
	
	# contact_form = ContactForm(None)
	# print('--- contact_form = ContactForm(None)')
	# print(contact_form)#
	
	# contact_form = ContactForm()
	# print('--- contact_form = ContactForm()')
	# print(contact_form)#
	###my part

	contact_form = ContactForm(request.POST or None)
	context = {
	"title": "Contact Page",
	"content": "This is contact page",
	"form": contact_form,
	"brand": "New brand name"
	}

	if contact_form.is_valid():
		print('--- print contact_form.cleaned_data')
		print(contact_form.cleaned_data)
	
	# if request.method == "POST":
	# 	print(type(request.POST))
	# 	print(request.POST.get('fullname'))
	# 	print(request.POST.get('email'))
	# 	print(request.POST.get('content'))
	return render(request, 'contact/view.html', context)




def login_page(request):
	form = LoginForm(request.POST or None)
	context = {
		"form": form
	}
	print("User logged-in is: ")
	print(request.user.is_authenticated())
	
	if form.is_valid():
		print('--- print login_form.cleaned_data')
		print(form.cleaned_data) #<-- dict key, value

		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get("password")
		user = authenticate(request, username=username, password=password)
		print(request.user.is_authenticated())
		print(user)

		if user is not None:
			print(request.user.is_authenticated())
			login(request, user)
			print("---after login---")
			print(request.user.is_authenticated())
			#redirect to a success page
			#context['form'] = LoginForm()
			return redirect("/login")
		else:
			# return an invalid login error message
			print("error")

		#print(context['form']) <-- to sam html bez wypelnionych pol
	return render(request, "auth/login.html", context)



User = get_user_model()
def register_page(request):
	form = RegisterForm(request.POST or None)
	print(form)
	context = {
		"form": form
	}
	if form.is_valid():
		print('--- print register form.cleaned_data')
		print(form.cleaned_data)

		username = form.cleaned_data.get("username")
		email	 = form.cleaned_data.get("email")
		password = form.cleaned_data.get("password")
		new_user = User.objects.create_user(username, email, password)
		print(new_user)

	return render(request, "auth/register.html", context)


def home_page_old(request):
	html_ = """
	<!doctype html>
	<html lang="en">
	  <head>
	    <title>Hello, world!</title>
	    <!-- Required meta tags -->
	    <meta charset="utf-8">
	    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

	    <!-- Bootstrap CSS -->
	    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.2/css/bootstrap.min.css" integrity="sha384-PsH8R72JQ3SOdhVi3uxftmaW6Vc51MKb0q5P2rRUpPvrszuE4W1povHYgTpBfshb" crossorigin="anonymous">
	  </head>
	  <body>
	  	<div class='text-center'>
	    	<h1>Hello, world!</h1>
	    </div>

	    <!-- Optional JavaScript -->
	    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
	    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
	    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.3/umd/popper.min.js" integrity="sha384-vFJXuSJphROIrBnz7yo7oB41mKfc8JzQZiCq4NCceLEaO4IHwicKwpJf9c9IpFgh" crossorigin="anonymous"></script>
	    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.2/js/bootstrap.min.js" integrity="sha384-alpBpkh1PFOepccYVYDB4do5UnbKysX5WZXm3XxPqe5iKTfUKjNkCk9SaVuEZflJ" crossorigin="anonymous"></script>
	  </body>
	</html>
	"""
	return HttpResponse(html_)
