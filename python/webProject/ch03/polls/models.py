#모델과 관련된 작업을 한다.
#데이터베이스 작업을 함

#primary key 는 시스템이 알아서 만들어 주기 때문에
#table 에서 idx는 별도로 작업하지 않아도 됨


from django.db import models

# Create your models here.

class Question(models.Model):
    question_text = models.CharField("질문 내용 ",max_length=200)
    #pub_date = models.DateTimeField('date published')
    #관리자 페이지의 내용 변경
    pub_date = models.DateTimeField('질문 생성일')

    def __str__(self):      #__str__ == toString
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

