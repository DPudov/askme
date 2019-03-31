from django.core.paginator import Paginator
from django.shortcuts import render, render_to_response
from django.template import RequestContext

from .models import Answer
from .models import Question


# Create your views here.

def login(request):
    return render(request, 'question/login.html', {})


def index(request):
    # if request.method == 'POST':
    #     form =
    questions_list = Question.objects.order_by('-create_date')
    paginator = Paginator(questions_list, 20)

    page = request.GET.get('page')

    questions = paginator.get_page(page)
    return render(request, "question/index.html", {
        "questions": questions,
    })


def question(request, id):
    quest = Question.objects.get(id=id)
    answers = Answer.objects.filter(question_id=id)
    Answer.objects.order_by('question_id')
    return render(request, "question/question.html", {
        "question": quest,
        "answers": answers
    })


def registration(request):
    return render(request, "question/registration.html", {

    })


def settings(request):
    return render(request, "question/settings.html", {

    })


def add_question(request):
    return render(request, "question/add_question.html", {

    })


def my_handler404(request):
    context = RequestContext(request)
    response = render_to_response('question/error404.html', context)
    response.status_code = 404
    return response


def my_handler500(request):
    context = RequestContext(request)
    response = render_to_response('question/error500.html', context)
    response.status_code = 500
    return response
