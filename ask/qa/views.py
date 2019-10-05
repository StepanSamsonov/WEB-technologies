from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.core.paginator import Paginator
from .models import Question


def test(request, *args, **kwargs):
    return HttpResponse('OK')

def page(request):
	paginator = Paginator(Question.objects.new(), 10)
	page = request.GET.get('page')
	
	try:
		page = int(page)
	except:
		page = 1

	questions = paginator.page(page)


	return render(request, 'page.html', {
		'questions': questions,
	})

def popular_page(request):
	paginator = Paginator(Question.objects.popular(), 10)
	page = request.GET.get('page')

	try:
		page = int(page)
	except:
		page = 1

	questions = paginator.page(page)

	return render(request, 'popular_page.html', {
		'questions': questions,
	})

def question_page(request, id):
	try:
		question = Question.objects.get(id=id)
	except Question.DoesNotExist:
		raise Http404('Not found')
	
	return render(request, 'question_page.html', {
		'question': question,
	})
