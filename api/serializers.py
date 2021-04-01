from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Question, Answer


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = [
            'id', 'owner', 'body', 'date_created', 'likes', 'question',
        ]


class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = [
            'id', 'owner', 'title', 'body', 'date_created', 'likes', 'answered', 'answers',
        ]


class UserSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)
    answers = AnswerSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'questions', 'answers', ]