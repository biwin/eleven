# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from mysite.books.models import Book


def search_form(request):
	return render_to_response('search/search_form.html')


def search(request):
	errors = []
	if 'q' in request.GET:
		q = request.GET['q']
		if not q:
			errors.append('Enter a search term')

		elif len(q) > 20:
			errors.append('Enter less than 20 characters including spaces.')

		else:
			books = Book.objects.filter(title__icontains=q)
			return render_to_response('search/search_results.html', {'books': books, 'query': q})
	return render_to_response('search/search_form.html', {'errors': errors})