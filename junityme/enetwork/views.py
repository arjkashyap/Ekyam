from django.shortcuts import render
from .forms import Question
from .models import *


def index(request):
    return render(request, 'enetwork/index.html')



class Addquestions(CreateView):
    model = Question
    fields = ['problem_title', 'problem_category', 'problem_description', 'problem_field']


def QuestionList(request):
    ques = Question.objects.all()
    return render(request, 'enetwork/questionlist.html', {'ques': ques})
