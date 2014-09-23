from django.http import HttpResponse, Http404
import datetime


def hello(request):
	return HttpResponse('Hello World!!')


def home(request):
		return HttpResponse("hey this is home!!")


def current_datetime(request):
	now = datetime.datetime.now()
	return HttpResponse(now)


def hours_ahead(request, offset):
	try:
		offset = int(offset)
	except ValueError:
		raise Http404()

	dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
	html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
	return HttpResponse(html)