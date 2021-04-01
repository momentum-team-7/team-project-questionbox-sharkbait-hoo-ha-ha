from rest_framework import generics
from .models import Question, Answer
from django.contrib.auth.models import User
from .serializers import QuestionSerializer, AnswerSerializer, UserSerializer
# Create your views here.


class QuestionList(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class AnswerList(generics.ListCreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

class AnswerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer    


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

