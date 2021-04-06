from django.db import models

# Create your models here.


class Question(models.Model):
    owner = models.ForeignKey(
        'auth.User', related_name='questions', on_delete=models.CASCADE)
    title = models.CharField(max_length=140, blank=True, null=True)
    body = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    likers = models.ManyToManyField('auth.User', related_name='question_likes')
    answered = models.BooleanField(default=False)

    class Meta:
        ordering = ['date_created']

    def __str__(self):
        return f"{self.title}"


class Answer(models.Model):
    owner = models.ForeignKey(
        'auth.User', related_name='answers', on_delete=models.CASCADE)
    body = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    likers = models.ManyToManyField('auth.User', related_name='answer_likes')
    question = models.ForeignKey(
        Question, related_name='answers', on_delete=models.CASCADE)

    class Meta:
        ordering = ['date_created']
