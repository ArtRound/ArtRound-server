from rest_framework import serializers
from .models import Review, Question, Answer, Notice, Favorites, User, ArtInfo
from drf_extra_fields.fields import Base64ImageField
from rest_framework_simplejwt.tokens import RefreshToken

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

class ArtInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtInfo
        fields = ('id','fcltyNm','weekdayOperOpenHhmm','weekdayOperColseHhmm','holidayOperOpenHhmm','holidayCloseOpenHhmm','rstdeInfo','adultChrge','yngbgsChrge','childChrge','rdnmadr','phoneNumber','homepageUrl','latitude','longitude')

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

