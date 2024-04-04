
from django.views.generic import ListView, DetailView
from .models import Question,Choice

class QuestionListView(ListView):
    model = Question



class ChoiceListView(ListView):
    model = Choice
    context_object_name = 'choice_list'  # 이 부분을 추가하여 컨텍스트 변수명을 설정합니다.
    template_name = 'ki_polls/choice_list.html'



