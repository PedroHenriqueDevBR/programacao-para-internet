from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=50)
    closed = models.BooleanField(default=False)
    pub_date = models.DateTimeField(auto_now=True)

    def close(self):
        self.closed = True

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices', null=True)
    choice_text = models.CharField(max_length=50)
    votes = models.IntegerField()

    def __str__(self):
        return self.choice_text
