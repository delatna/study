from django.conf.urls import url
from . import views

app_name = "polls"
#URLconf 코딩 한다

urlpatterns = [
    #127.0.0.1:8888/polls/
    url(r'^$', views.index, name='index'),

    #polls/3    3번 설문에 대한 상세보기
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),

    # polls/3/results/    3번 설문에 대한 결과보기, result.html
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),

# polls/3/vote/    3번 설문에 대한 투표 실행, vote.html
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),

]