from django.views.generic import ListView
from .models import Question, Choice

class QuestionListView(ListView):
    model = Question
    context_object_name = 'question_list'  # question_list 변수를 템플릿에서 사용할 수 있도록 설정합니다.

class ChoiceListView(ListView):
    model = Choice
    context_object_name = 'choices'  # choices 변수를 템플릿에서 사용할 수 있도록 설정합니다.
    template_name = 'ki_polls/choice_list.html'

    def get_queryset(self):
        # URL 매개변수인 category를 가져옵니다.
        category = self.kwargs['category']
        # category에 해당하는 질문을 가져옵니다.
        question = Question.objects.filter(category=category).first()
        if question:
            # 질문에 해당하는 선택 항목을 반환합니다.
            return question.choice_set.all()
        return Choice.objects.none()
