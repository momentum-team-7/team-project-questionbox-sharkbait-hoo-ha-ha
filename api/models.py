from django.db import models

# Create your models here.


class Question(models.Model):
    owner = models.ForeignKey(
        'auth.User', related_name='questions', on_delete=models.CASCADE)
    title = models.CharField(max_length=140, blank=True, null=True)
    body = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    answered = models.BooleanField(default=False)


class Answer(models.Model):
    owner = models.ForeignKey(
        'auth.User', related_name='answer', on_delete=models.CASCADE)
    body = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    question = models.ForeignKey(
        Question, related_name='question', on_delete=models.CASCADE)
