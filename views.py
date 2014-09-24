from django.http import HttpResponse, Http404
from django.template import Context
from django.template.loader import get_template
from django.shortcuts import render_to_response
import datetime


def hello(request):
	return HttpResponse('Hello World!!')


def home(request):
	return HttpResponse("hey this is home!!")

# traditional way
# def current_datetime(request):
# 	now = datetime.datetime.now()
# 	text = Template("it is now {{ current_time }} ")
# 	html = text.render(Context({'current_time' : now}))
# 	return HttpResponse(html)

# render to get_template()
# def current_datetime(request):
# 	now = datetime.datetime.now()
# 	t = get_template('current_datetime.html')
# 	html = t.render(Context({'current_time': now}))
# 	return HttpResponse(html)


def current_datetime(request):
	now = datetime.datetime.now()
	return render_to_response('current_datetime.html', {'current_time': now})

def hours_ahead(request, offset):
	try:
		offset = int(offset)
	except ValueError:
		raise Http404()

	dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
	html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
	return HttpResponse(html)