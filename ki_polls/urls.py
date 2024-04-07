from django.urls import path
from . import views

app_name = "ki_polls"

urlpatterns = [
    path("", views.QuestionListView.as_view(), name="index"),
    path('choice/<str:category>/', views.ChoiceListView.as_view(), name='choice_list'),
]