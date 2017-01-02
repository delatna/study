# file name : ch03/polls/views.py

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpRequest
from django.core.urlresolvers import reverse
from polls.models import Question, Choice

#지금까지 함수를 이용해서 index, results, detail, vote 를 만들었는데
# 그 방법 외에 클래스뷰로 만들어 사용하는 것이 더 편하다
#이것을 위해 import 하나가 필요

from django.views import generic

class indexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """최근 5개의 설문 목록을 표시합니다"""
        return Question.objects.order_by("-pub_date")[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"
# Create your views here.
# ch03/templates/polls/index.html 에서 latest_question_list 를 이용했다
# 그 latest_question_list 를 만들기

def index(request):
    latest_question_list = Question.objects.all().order_by('-pub_date')[:5]
    #즉 역순으로 5개를 보여준다
    context = {'latest_question_list':latest_question_list}
    # latest_question_list 라는 키값에 latest_question_list 라는 리스트를 value
    # 로 갖는 Diction Type 데이터를 만들어줌
    return render(request, 'polls/index.html', context)
    # 즉 직전에 만든 ch03/templates/polls/index.html파일을 만드는데
    #여기서 만든 latest_question_list 를 이용해서 파일을 만들어라 !

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    print("question = ", question)
    print("question id = ", question_id)
    print("question text = ", question.question_text)
    return render(request, 'polls/detail.html',{'question':question})

#vote 에 해당하는 코드를 추가
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])

    except(KeyError, Choice.DoesNotExist):
        return render(request, "polls/detail.html",{
            "question":question,
            "error_message":"Please Select a Choice",

        })
    else:
        selected_choice.votes = selected_choice.votes + 1
        selected_choice.save()
        #투표 숫자 처리가 완료되었으므로, 결과보기 페이지로 강제 이동(Redirect)
                                            #polls/3/results
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

# results 해당하는 코드를 추가
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question":question})
