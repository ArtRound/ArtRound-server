from rest_framework import serializers
from .models import Review, Question, Answer, Notice, Favorites
from drf_extra_fields.fields import Base64ImageField


class ReviewSerializer(serializers.ModelSerializer):
    image = Base64ImageField(use_url=True, max_length=None)
    class Meta:
        model = Review
        fields = ('id', 'title', 'content', 'useremail', 'updated_at', 'image')


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'useremail', 'type', 'title', 'content', 'updated_at')

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('id', 'content', 'updated_at')


class NoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notice
        fields = ('id', 'title', 'content', 'updated_at')


class FavoritesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorites
        fields = ('id', 'title', 'content', 'updated_at')
