from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.template import loader

from .models import Question, Choice

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
    """ 
    Displays results for a particular question.
    NB: This view is similiar to to detail view
     """
    question = get_object_or_404(Question, pk=question_id)
    context = dict(question=question)
    return render(request, "polls/result.html", context)


def vote(request, question_id):
    """ Handles voting for a particular choice in a particular question. """
    # question = get_object_or_404(Question, pk=question_id)
    try:
        question = Question.objects.get(pk=question_id)
        choice_id = request.POST['choice']
        selected_choice = question.choice_set.get(pk=choice_id)
    except Question.DoesNotExist:
        # raise Http404("Question cannot be found.")
        context = dict(question=question, error_message="Question cannot be found.")
        return render(request, "polls/results.html", context)
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form
        context = dict(question=question, error_message="You didn't select a choice.")
        return render(request, "polls/detail.html", context)
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question_id)))
        # Instead of polls/3/results, use polls:result,args=3,


def echo(request, text):
    """ Any extra text string is echoed in the webpage.  """
    return HttpResponse(text)