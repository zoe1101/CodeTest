# 改良视图，删除旧的 index, detail, 和 results 视图，并用 Django 的通用视图代替。
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Choice, Question

from django.utils import timezone


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]
        # Question.objects.filter(pub_date__lte=timezone.now()) 返回一个查询集，其中包含 pub_date小于或等于 - 即早于或等于 - timezone.now 的问题。


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


def vote(request, question_id):
    '''
    处理提交的投票数据
    :param request:
    :param question_id:
    :return:
    '''
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
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

#
# from django.http import HttpResponse, HttpResponseRedirect
# from django.template import loader
# from django.http import Http404
# from django.shortcuts import get_object_or_404, render
# from django.urls import reverse
# from django.utils.regex_helper import Choice
#
# from .models import Question
#
#
# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {
#         'latest_question_list': latest_question_list,
#     }
#
#     return render(request, 'polls/index.html', context)
#     # render是快捷函数，等同于下列两行
#     # template = loader.get_template('polls/index.html')
#     # return HttpResponse(template.render(context, request))
#
#
# def detail(request, question_id):
#     '''
#     投票详情视图
#     :param request:
#     :param question_id:
#     :return:
#     '''
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question': question})
#     # get_object_or_404是快捷函数，等于下面4行
#     # try:
#     #     question = Question.objects.get(pk=question_id)
#     # except Question.DoesNotExist:
#     #     raise Http404("Question does not exist")
#     return render(request, 'polls/detail.html', {'question': question})
#
#
# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})
#
#
