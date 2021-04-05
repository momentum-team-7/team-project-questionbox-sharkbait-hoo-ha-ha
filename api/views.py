from rest_framework import generics, permissions, filters
from .permissions import IsOwnerOrReadOnly
from .models import Question, Answer
from django.contrib.auth.models import User
from django.contrib.postgres.search import SearchVector
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .serializers import *


class QuestionList(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = Question.objects.all()
        search_input = self.request.query_params.get('search')
        if search_input is not None:
            queryset = Question.objects.annotate(search=SearchVector(
                'owner', 'title', 'body')).filter(search=search_input)
        return queryset

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user, answers=[])


class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    # permission_classes = [permissions.IsAuthenticated]
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class AnswerList(generics.ListCreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = Answer.objects.all()
        search_input = self.request.query_params.get('search')
        if search_input is not None:
            queryset = Answer.objects.annotate(
                search=SearchVector('owner', 'body')).filter(search=search_input)
        return queryset

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class AnswerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
