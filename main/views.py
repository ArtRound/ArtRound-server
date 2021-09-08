from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404

from .serializers import ReviewSerializer, QuestionSerializer
from .models import Review, Question


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


class QuestionList(APIView):
    # 블로그 목록 보여줄 때
    def get(self, request):
        questions = Question.objects.all()
        # 여러개 객체 serialize하려면 many=True
        # TO JSON Format
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)

    # 새 글 작성시
    def post(self, request):
        serializer = QuestionSerializer(
            data=request.data)  # request.data는 사용자 입력 데이터
        if serializer.is_valid():  # 유효성 검사
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
