from django.db.models.query import QuerySet
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Question, Answer


class AnswerSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    owner_id = serializers.ReadOnlyField(source='owner.id')
    question_title = serializers.ReadOnlyField(source='question.title')

    class Meta:
        model = Answer
        fields = [
            'id', 'owner', 'owner_id', 'body', 'date_created', 'likes', 'question', 'question_title', 'likers',
        ]


class AnswerSearchSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    owner_id = serializers.ReadOnlyField(source='owner.id')

    class Meta:
        model = Answer
        fields = [
            'id', 'owner', 'owner_id', 'body'
        ]


class QuestionSerializer(serializers.ModelSerializer):
    # answers = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    answers = AnswerSerializer(many=True, read_only=True)
    owner = serializers.ReadOnlyField(source='owner.username')
    owner_id = serializers.ReadOnlyField(source='owner.id')

    class Meta:
        model = Question
        fields = [
            'id', 'owner', 'owner_id', 'title', 'body', 'date_created', 'likes', 'answered', 'answers', 'likers',
        ]


class QuestionSearchSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    owner_id = serializers.ReadOnlyField(source='owner.id')

    class Meta:
        model = Question
        fields = [
            'id', 'owner', 'owner_id', 'title', 'body',
        ]


class UserSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)
    answers = AnswerSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'questions', 'answers', ]


class SearchSerializer(serializers.Serializer):
    questions = QuestionSearchSerializer(many=True, read_only=True)
    answers = AnswerSearchSerializer(many=True, read_only=True)

    class Meta:
        fields = ['questions', 'answers']
