from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *

class Questions(ListView):
    model = Question
    paginate_by = 10
    context_object_name = 'questions'


class Qu_detail(DetailView):
    model = Question
    context_object_name = 'question'
    template_name = 'mylinkedtest/qu_detail.html'




class Answers(ListView):
    model = Answer


class QuestionDetailView(DetailView):
    model = Question

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form_answer"] = 1
        return context
