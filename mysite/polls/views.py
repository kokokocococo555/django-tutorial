# from django.template import loader
# from django.http import Http404
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Choice, Question


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
# def detail(request, question_id):
    # question = get_object_or_404(Question, pk=question_id)
    # return render(request, 'polls/detail.html', {'question': question})

    # よくある処理なので「汎用ビュー(generic view)」が用意されている(https://docs.djangoproject.com/ja/2.2/intro/tutorial04/)
    # 1. URLを介してパラメータが渡される
    # 2. -> パラメータに従ってデータベースからデータを取り出す
    # 3. -> テンプレートをロードする
    # 4. -> レンダリングしたテンプレートを返す 
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    # 複数人のユーザーが同時に投票しようとするケースにバグがある
    # 同時に投票された票がなかったことになってしまう「競合状態」にある
    # 解決策：https://docs.djangoproject.com/ja/2.2/ref/models/expressions/#avoiding-race-conditions-using-f
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # reverse(制御を渡したいビューの名前, 与えるURLパターンの位置引数)
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
