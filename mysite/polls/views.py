from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader

from .models import Question

# Create your views here.

def index(request):
    """ Displays the latest few questions. """
    # return HttpResponse("Hello, world. You're at the polls index.")
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = dict(
        latest_question_list=latest_question_list,
        )
    # return HttpResponse(template.render(context, request))
    return render(request, 'polls/index.html', context)

def request_dir(request):
    """ Displays statistical information about request object. """
    context = dict(req=dir(request))
    return render(request, 'polls/request_dir.html', context=context)
    # return HttpResponse(str(dir(request)))

def detail(request, question_id):
    """ Displays a question text, with no results but with a form to vote. """
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    context = dict(question=question)
    return render(request, "polls/detail.html", context)

def results(request, question_id):
    """ Displays results for a particular question. """

def vote(request, question_id):
    """ Handles voting for a particular choice in a particular question. """

def echo(request, text):
    """ Any extra text string is echoed in the webpage.  """
    return HttpResponse(text)