from dataclasses import field
from rest_framework import serializers
from .models import Review, Question, Answer, Notice, Favorites, User, ArtInfo, Visited
from rest_framework_simplejwt.tokens import RefreshToken

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = "__all__"

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = "__all__"


class NoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notice
        fields = "__all__"


class FavoritesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorites
        fields = "__all__"

class ArtInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtInfo
        fields = "__all__"

class VisitedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visited
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class CustomTokenRefreshSerializer(serializers.Serializer):
    refresh_token = serializers.CharField()

    def validate(self, attrs):
        refresh = RefreshToken(attrs['refresh_token'])
        data = {'access_token': str(refresh.access_token)}

        return data

