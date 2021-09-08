from rest_framework import serializers
from .models import Review, Question


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'title', 'content', 'useremail', 'updated_at')


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'useremail', 'type', 'title', 'content', 'updated_at')
