from django.db.models.query import QuerySet
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Question, Answer





class AnswerSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    owner_id = serializers.ReadOnlyField(source='owner.id')

    class Meta:
        model = Answer
        fields = [
            'id', 'owner', 'owner_id', 'body', 'date_created', 'likes', 'question',
        ]


class QuestionSerializer(serializers.ModelSerializer):
    # answers = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    answers = AnswerSerializer(many=True, read_only=True)
    owner = serializers.ReadOnlyField(source='owner.username')
    owner_id = serializers.ReadOnlyField(source='owner.id')

    class Meta:
        model = Question
        fields = [
            'id', 'owner', 'owner_id', 'title', 'body', 'date_created', 'likes', 'answered', 'answers',
        ]


class UserSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)
    answers = AnswerSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'questions', 'answers', ]
