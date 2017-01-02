from django.contrib import admin

# Register your models here.
#admin 페이지에서의 동작을 등록

from polls.models import Question, Choice

#원래 모양
#admin.site.register(Question)
#admin.site.register(Choice)

#class ChoiceInline(admin.StackedInline):   #항목들을 쌓아서 아래로 보여주기

class ChoiceInline(admin.TabularInline):    #항목들을 테이블 형태로 보여주기
    model = Choice
    extra = 2 #현재 등록된 데이터 수 + 2

class QuestionAdmin(admin.ModelAdmin):
    #fields = ['pub_data', 'question_text']
    # 두개의 카테고리로 나눠주기
    fieldsets = [
        ('Question Statement',{'fields':['question_text']}),
        ('Data information',{'fields':['pub_date']}),
    ]
    
    #folding
    fieldsets = [
        ('Question Statement',{'fields':['question_text']}),
        ('Data information',{'fields':['pub_date'],'classes':['collapse']}),
    ]
    inlines = [ChoiceInline]
    #질문 목록의 항목을 선택
    list_display = ('question_text','pub_date')

    #필터 추가하기
    list_filter = ['pub_date']

    #검색 창(검색 박스)
    search_fields = ['question_text']    #제목 검색
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)


