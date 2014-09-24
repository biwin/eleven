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
# (or)	t = get_template('subdir/current_datetime.html')
# 	html = t.render(Context({'current_time': now}))
# 	return HttpResponse(html)


def current_datetime(request):
	current_time = datetime.datetime.now()
	name = "biwin"
	return render_to_response('current_datetime.html', locals())
# (or) return render_to_response('subdir/current_datetime.html', locals())



def hours_ahead(request, offset):
	try:
		offset = int(offset)
	except ValueError:
		raise Http404()

	date_time = datetime.datetime.now() + datetime.timedelta(hours=offset)
	return render_to_response('hours_ahead.html', locals())