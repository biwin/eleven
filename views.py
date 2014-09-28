import datetime

from django.http import HttpResponse, Http404
from django.template import Context, loader, RequestContext
from django.shortcuts import render_to_response


def hello(request):
	return HttpResponse('Hello World!!')


def home(request):
	return HttpResponse("hey this is home!!")


# traditional way
# def current_datetime(request):
# now = datetime.datetime.now()
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


def test_http(request):
	# hu = request.META.get('HTTP_USER_AGENT', 'unknown')
	# return HttpResponse(hu)
	values = request.META.items()
	values.sort()
	html = []
	for k, v in values:
		html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
	return HttpResponse('<table>%s</table>' % '\n'.join(html))


def processor(request):
	""" A Context processor to provide 'name', 'user' and 'ip_address """
	return {
		'name': 'myName',
		'user': request.user,
		'ip_address': request.META['REMOTE_ADDR']
	}


def view_1(request):
	t = loader.get_template('advancedtemplates/template1.html')
	c = RequestContext(request, {'message': 'happy day from view_1'}, processors=[processor])
	html = t.render(c)
	return HttpResponse(html)


def view_2(request):
	t = loader.get_template('advancedtemplates/template2.html')
	c = RequestContext(request, {'message': 'happy day from view_2'}, processors=[processor])
	html = t.render(c)
	return HttpResponse(html)