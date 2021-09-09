from rest_framework import serializers
from .models import Review, Question, Notice


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'title', 'content', 'useremail', 'updated_at')


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'useremail', 'type', 'title', 'content', 'updated_at')


class NoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notice
        fields = ('id', 'title', 'content', 'updated_at')