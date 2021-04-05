from rest_framework import generics, permissions, filters
from .permissions import IsOwnerOrReadOnly
from .models import Question, Answer
from django.contrib.auth.models import User
from django.contrib.postgres.search import SearchVector
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .serializers import QuestionSerializer, AnswerSerializer, UserSerializer, SearchSerializer, QuestionSearchSerializer, AnswerSearchSerializer

from itertools import chain


class Search(generics.ListAPIView):
    # search_fields = ['answers__body', 'questions__title', 'questions__body']
    # filter_backends = (filters.SearchFilter,)
    # queryset = list(chain(Question.objects.all(), Answer.objects.all()))
    # serializer_class = SearchSerializer
    # currently searches over Qs and As, but only displays As. gotta update. (can also do one that only searches/displays Qs)
    def get_queryset(self):

        queryset = Question.objects.annotate(search=SearchVector(
            'body', 'title', )).filter(search=self.request.query_params.get('search'))
        # queryset.add(Answer.objects.annotate(search=SearchVector('body')).filter(
        # search=self.request.query_params.get('search')))
        return queryset
    serializer_class = SearchSerializer

    # filter_backends = (filters.SearchFilter,)
    # search_fields = ['title', 'body', ]


class QuestionList(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

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
