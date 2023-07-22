from django.contrib import admin
from .models import Question, Answer


class Answers(admin.TabularInline):
    model = Answer


class Questions(admin.ModelAdmin):
    inlines = [Answers]


# Register your models here.
admin.site.register(Question, Questions)
admin.site.register(Answer)
