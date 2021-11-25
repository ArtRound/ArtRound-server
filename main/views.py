from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404

from .serializers import ReviewSerializer, QuestionSerializer, NoticeSerializer, FavoritesSerializer
from .models import Review, Question, Notice, Favorites


class ReviewList(APIView):
    # 블로그 목록 보여줄 때
    def get(self, request):
        reviews = Review.objects.all()
        # 여러개 객체 serialize하려면 many=True
        # TO JSON Format
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)

    # 새 글 작성시
    def post(self, request):
        serializer = ReviewSerializer(
            data=request.data)  # request.data는 사용자 입력 데이터
        if serializer.is_valid():  # 유효성 검사
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReviewDetail(APIView):
    # Review 객체 가져오기
    def get_object(self, pk):
        try:
            return Review.objects.get(pk=pk)
        except Review.DoesNotExist:
            raise Http404

    # Review detail 보기
    def get(self, request, pk, format=None):
        review = self.get_object(pk)
        serializer = ReviewSerializer(review)
        return Response(serializer.data)

    # Review 수정하기
    def put(self, request, pk, format=None):
        review = self.get_object(pk)
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid():  # 유효성 검사
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Review 삭제하기
    def delete(self, request, pk, format=None):
        review = self.get_object(pk)
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#--------------------------------------------------------------------------------

class QuestionList(APIView):
    # 블로그 목록 보여줄 때
    def get(self, request):
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)

    # 새 글 작성시
    def post(self, request):
        serializer = QuestionSerializer(
            data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionDetail(APIView):
    def get_object(self, pk):
        try:
            return Question.objects.get(pk=pk)
        except Question.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        question = self.get_object(pk)
        serializer = QuestionSerializer(question)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        question = self.get_object(pk)
        serializer = QuestionSerializer(question, data=request.data)
        if serializer.is_valid():  # 유효성 검사
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        question = self.get_object(pk)
        question.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#--------------------------------------------------------------------------------

class NoticeList(APIView):
    # 공지사항 목록
    def get(self, request):
        notices = Notice.objects.all()
        serializer = NoticeSerializer(notices, many=True)
        return Response(serializer.data)

    # Notice Create
    def post(self, request):
        serializer = NoticeSerializer(data=request.data)  # request.data : 사용자 입력 데이터
        if serializer.is_valid():  # 유효성 검사
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NoticeDetail(APIView):
    # Notice 객체 가져오기
    def get_object(self, pk):
        try:
            return Notice.objects.get(pk=pk)
        except Notice.DoesNotExist:
            raise Http404

    # Notice Read
    def get(self, request, pk, format=None):
        notice = self.get_object(pk)
        serializer = NoticeSerializer(notice)
        return Response(serializer.data)

    # Notice Update
    def put(self, request, pk, format=None):
        notice = self.get_object(pk)
        serializer = NoticeSerializer(notice, data=request.data)
        if serializer.is_valid():  # 유효성 검사
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Notice Delete
    def delete(self, request, pk, format=None):
        notice = self.get_object(pk)
        notice.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
#--------------------------------------------------------------------------------

class FavoritesList(APIView):
    # 즐겨찾기 목록
    def get(self, request):
        favorites = Favorites.objects.all()
        serializer = FavoritesSerializer(favorites, many=True)
        return Response(serializer.data)

    # Favorites Create
    def post(self, request):
        serializer = FavoritesSerializer(data=request.data)  # request.data : 사용자 입력 데이터
        if serializer.is_valid():  # 유효성 검사
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NoticeDetail(APIView):
    # Favorites 객체 가져오기
    def get_object(self, pk):
        try:
            return Favorites.objects.get(pk=pk)
        except Favorites.DoesNotExist:
            raise Http404

    # Favorites Read
    def get(self, request, pk, format=None):
        favorites = self.get_object(pk)
        serializer = FavoritesSerializer(favorites)
        return Response(serializer.data)

    # Favorites Update 근데 이게 필요할까
    def put(self, request, pk, format=None):
        favorites = self.get_object(pk)
        serializer = FavoritesSerializer(favorites, data=request.data)
        if serializer.is_valid():  # 유효성 검사
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Favorites Delete
    def delete(self, request, pk, format=None):
        favorites = self.get_object(pk)
        favorites.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)