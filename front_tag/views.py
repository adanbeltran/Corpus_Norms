from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse , Http404 , HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist
from django.views import generic

from .models import Question, Choice

class IndexView(generic.ListView):
    template_name = 'front_tag/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]

"""def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'front_tag/index.html', context)"""

class DetailView(generic.DetailView):
    model = Question
    template_name = 'front_tag/detail.html'

"""def detail(request, question_id):
    #return HttpResponse("You're looking at question %s." % question_id)
    #try:
    #    question = Question.objects.get(pk=question_id)
    #except Question.DoesNotExist:
    #    raise Http404("Question does not exist ....")
    #return render(request, 'front_tag/detail.html',{'question': question})
    question = get_object_or_404(Question , pk=question_id)
    return render(request,'front_tag/detail.html',{'question':question})"""

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'front_tag/results.html'

"""def results(request, question_id):
    #response = "You're looking at the results of question %s."
    #return HttpResponse(response % question_id)
    question = get_object_or_404(Question , pk=question_id )
    #return render(request,'front_tag', {'question':question})
    return render(request, 'front_tag/results.html',{'question': question})"""

def vote(request, question_id):
    #return HttpResponse("You're voting on question %s." % question_id)
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except ObjectDoesNotExist:
        # Redisplay the question voting form.
        return render(request, 'front_tag/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('front_tag:results', args=(question.id,)))
