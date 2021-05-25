from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
# from django.template import loader
from .models import Choice, Question, Thought
from django.http import Http404
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .forms import ThoughtForm
from django.forms import modelformset_factory


# Title: Working with Forms
# Author: Django Documentation
# Date: 2-10-21
# Code version: n/a
# URL: https://docs.djangoproject.com/en/3.1/topics/forms/
# Software License: n/a
# Comments: Referenced to make manage_thoughts, get_thoughts

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions. (not including those set to be
        published in the future)"""
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]


class ThoughtView(generic.ListView):
    model = Thought
    template_name = 'polls/thoughts.html'
    context_object_name = 'latest_thought_list'


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def thoughts_sub(request):
    return render(request, 'polls/thoughts_sub.html')


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponse Redirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))


# This function does not end up being used
def get_thoughts(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ThoughtForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/polls/thoughts/list')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ThoughtForm()

    return render(request, 'polls/thoughts_sub.html', {'form': form})


def manage_thoughts(request):
    if request.method == 'POST':
        formset = ThoughtForm(request.POST or None)
        if formset.is_valid():
            formset.save()
            formset = ThoughtForm()  # Clears text after submission
            return HttpResponseRedirect(reverse('polls:thoughts', ))
    else:
        formset = ThoughtForm()
    return render(request, 'polls/thoughts_sub.html', {'formset': formset})
