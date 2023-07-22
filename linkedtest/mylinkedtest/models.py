from django.db import models


class Question(models.Model):
    text = models.TextField(max_length=500)
    q_number = models.IntegerField()
    help_link = models.CharField(max_length=500, default="-")
    comment = models.TextField(max_length=500, default="-")

    def get_answers(self):
        return Answer.objects.filter(question__id=self.id)

    def get_right_answer(self):
        return Answer.objects.filter(question__id=self.id, a_right=True)

    def get_count_questions(self):
        return Question.objects.all().count()

    def all_questions(self):
        return Question.objects.all()

    def __str__(self):
        return f"Q{self.q_number}. {self.text} "



class Answer(models.Model):
    a_number = models.IntegerField()
    text = models.TextField(max_length=500)
    a_right = models.BooleanField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)



