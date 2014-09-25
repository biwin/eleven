# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response


def search_form(request):
	return render_to_response('searchform.html')


def search(request):
	if 'q' in request.GET:
		message = 'You searched for: %r' % request.GET['q']
	else:
		message = 'You submitted an empty form!!'
	return HttpResponse(message)

# 123