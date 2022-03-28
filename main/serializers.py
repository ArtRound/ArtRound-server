from dataclasses import field
from rest_framework import serializers
from .models import Review, Image, Question, Answer, Notice, Favorites, User, ArtInfo, Visited
from rest_framework_simplejwt.tokens import RefreshToken
from drf_extra_fields.fields import Base64ImageField

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['image']

class ReviewSerializer(serializers.ModelSerializer):
    image = Base64ImageField(use_url=True, max_length=None)
    
    class Meta:
        model = Review
        fields = ['id', 'title', 'content', 'user_id', 'art_info_id', 'updated_at', 'heart', 'image']


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

