from rest_framework import serializers
from .models import Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'title', 'content', 'updated_at')


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'useremail', 'type', 'title', 'content', 'updated_at')
