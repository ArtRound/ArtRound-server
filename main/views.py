from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from django.db.models import Count
from dotenv import load_dotenv
import os, requests, json, jwt

import requests
from django.shortcuts import redirect
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.http import JsonResponse
from json.decoder import JSONDecodeError
from dj_rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.kakao import views as kakao_view
from allauth.socialaccount.providers.google import views as google_view
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from allauth.socialaccount.models import SocialAccount

from .serializers import ReviewSerializer, QuestionSerializer, AnswerSerializer, NoticeSerializer, FavoritesSerializer
from .models import Review, Question, Answer, Notice, Favorites, User


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
class AnswerList(APIView):
    def get(self, request):
        answers = Answer.objects.all()
        serializer = AnswerSerializer(answers, many=True)
        return Response(serializer.data)

    # 새 글 작성시
    def post(self, request):
        serializer = AnswerSerializer(
            data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AnswerDetail(APIView):
    def get_object(self, pk):
        try:
            return Answer.objects.get(pk=pk)
        except Answer.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        answer = self.get_object(pk)
        serializer = AnswerSerializer(answer)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        answer = self.get_object(pk)
        serializer = AnswerSerializer(answer, data=request.data)
        if serializer.is_valid():  # 유효성 검사
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        answer = self.get_object(pk)
        answer.delete()
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


class FavoritesDetail(APIView):
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
     
#--------------------------------------------------------------------------------

KAKAO_CALLBACK_URI = 'http://localhost:3000/main/login/kakao'

def kakao_login(request):
    rest_api_key = getattr(settings, 'KAKAO_REST_API_KEY')
    return redirect(
        f"https://kauth.kakao.com/oauth/authorize?client_id={rest_api_key}&redirect_uri={KAKAO_CALLBACK_URI}&response_type=code"
    )

class KakaoLogin(SocialLoginView):
    adapter_class = kakao_view.KakaoOAuth2Adapter
    client_class = OAuth2Client
    callback_url = KAKAO_CALLBACK_URI  

    def post(self, request):
        load_dotenv(verbose=True)
        SECRET_KEY = os.getenv("SECRET_KEY")
        ALGORITHM = os.getenv("ALGORITHM")
        
        kakao_access_token = json.loads(request.body)
        print(kakao_access_token)
        
        url = "https://kapi.kakao.com/v2/user/me"
        real_code = kakao_access_token["params"]["code"]

        headers = {
                "Authorization":f"Bearer {real_code}",
                "Content-type":"application/x-www-form-urlencoded; charset=utf-8"
            }
        
        kakao_response = requests.post(url, headers=headers)
        kakao_response = json.loads(kakao_response.text)

        # 새로 가입했을 때
        if not User.objects.filter(id = kakao_response['id']).exists():
            print('새로 가입')
            user = User.objects.create(
                id = kakao_response['id'],
       
            )
            q = User.objects.annotate(Count("id"))
            print(q.count())      
                
            jwt_token = jwt.encode({'id':kakao_response['id']}, SECRET_KEY, ALGORITHM)
            print(jwt_token,type(jwt_token))
            if type(jwt_token) is bytes : 
                jwt_token = jwt_token.decode('utf-8')
                print(jwt_token, "fixed")
            # res = JsonResponse({"result":"false","id":kakao_response["id"],"email":kakao_response['kakao_account'].get('email',None),})
            res = JsonResponse({"result":"false","id":kakao_response["id"], "name": None, "age":0, "gender":None})

            res["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
            res["Access-Control-Allow-Credentials"] = "true"
            # res["Access-Control-Allow-Origin"] = "https://1n1n.io"
            res["Acess-Control-Max-Age"] = "1000"
            res["Access-Control-Allow-Headers"] = "X-Requested-With, Origin, X-Csrftoken, Content-Type, Accept"
            res.set_cookie(key="jwt_token", value=jwt_token, samesite=None, httponly=True, secure=True)
            return res

        # 이미 가입되어있을 때
        else:
            print('가입되어있음')
            q = User.objects.annotate(Count("id"))
            print(q.count())
            user = User.objects.filter(id = kakao_response['id'])
            jwt_token = jwt.encode({'id':kakao_response['id']}, SECRET_KEY, ALGORITHM)
            print(jwt_token,type(jwt_token))
            if type(jwt_token) is bytes : 
                jwt_token = jwt_token.decode('utf-8')
                print(jwt_token,"fixed")
            print(user)
            res = JsonResponse({"result":"true", "jwt_token": jwt_token, "id":kakao_response["id"],  "name": user.id, "age":user.age, "gender":user.gender})
            res["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
            res["Access-Control-Allow-Credentials"]="true"
            # res["Access-Control-Allow-Origin"] = "https://1n1n.io"
            res["Acess-Control-Max-Age"] = "1000"
            res["Access-Control-Allow-Headers"] = "X-Requested-With, Origin, X-Csrftoken, Content-Type, Accept"
            res.set_cookie(key="jwt_token",value=jwt_token,samesite=None,httponly=True,secure=True)
            return res    



#--------------------------------------------------------------------------------

GOOGLE_CALLBACK_URI = 'http://localhost:3000/main/login/google/callback'
state = "a9dfjGJwkAQek3G"

def google_login(request):
    # Code Request
    scope = "https://www.googleapis.com/auth/userinfo.email"
    client_id = getattr(settings, "SOCIAL_AUTH_GOOGLE_CLIENT_ID")
    return redirect(f"https://accounts.google.com/o/oauth2/v2/auth?client_id={client_id}&response_type=code&redirect_uri={GOOGLE_CALLBACK_URI}&scope={scope}")
# 이 함수와 매핑된 url로 들어가면, client_id, redirect uri 등과 같은 정보를 
# url parameter로 함께 보내 리다이렉트한다. 
# 그러면 구글 로그인 창이 뜨고, 알맞은 아이디, 비밀번호로 진행하면 
# Callback URI로 Code값이 들어가게 된다.

def google_callback(request):
    client_id = getattr(settings, "SOCIAL_AUTH_GOOGLE_CLIENT_ID")
    client_secret = getattr(settings, "SOCIAL_AUTH_GOOGLE_SECRET")
    code = request.GET.get('code')

    # Access Token Request
    # 받은 Code로 Google에 Access Token 요청
    token_req = requests.post(
        f"https://oauth2.googleapis.com/token?client_id={client_id}&client_secret={client_secret}&code={code}&grant_type=authorization_code&redirect_uri={GOOGLE_CALLBACK_URI}&state={state}")
    token_req_json = token_req.json()
    error = token_req_json.get("error")
    if error is not None:
        raise JSONDecodeError(error)
    access_token = token_req_json.get('access_token')

    # Email Request
    # Access Token으로 Email 값을 Google에게 요청
    email_req = requests.get(
        f"https://www.googleapis.com/oauth2/v1/tokeninfo?access_token={access_token}")
    email_req_status = email_req.status_code
    if email_req_status != 200:
        return JsonResponse({'err_msg': 'failed to get email'}, status=status.HTTP_400_BAD_REQUEST)
    email_req_json = email_req.json()
    email = email_req_json.get('email')
    
    # Signup or Signin Request
    # 전달받은 Email, Access Token, Code를 바탕으로 회원가입/로그인 진행
    try:
        user = User.objects.get(email=email)
        # 기존에 가입된 유저의 Provider가 google이 아니면 에러 발생, 맞으면 로그인
        # 다른 SNS로 가입된 유저
        social_user = SocialAccount.objects.get(user=user)
        if social_user is None:
            return JsonResponse({'err_msg': 'email exists but not social user'}, status=status.HTTP_400_BAD_REQUEST)
        if social_user.provider != 'google':
            return JsonResponse({'err_msg': 'no matching social type'}, status=status.HTTP_400_BAD_REQUEST)
        
        # 기존에 Google로 가입된 유저
        data = {'access_token': access_token, 'code': code}
        accept = requests.post(
            f"http://localhost:3000/main/login/google/finish/", data=data)
        accept_status = accept.status_code
        if accept_status != 200:
            return JsonResponse({'err_msg': 'failed to signin'}, status=accept_status)
        accept_json = accept.json()
        accept_json.pop('user', None)
        return JsonResponse(accept_json)

    except User.DoesNotExist:
        # 기존에 가입된 유저가 없으면 새로 가입
        data = {'access_token': access_token, 'code': code}
        accept = requests.post(
            f"http://localhost:3000/main/login/google/finish/", data=data)
        accept_status = accept.status_code
        if accept_status != 200:
            return JsonResponse({'err_msg': 'failed to signup'}, status=accept_status)
        accept_json = accept.json()
        accept_json.pop('user', None)
        return JsonResponse(accept_json)

class GoogleLogin(SocialLoginView):
    adapter_class = google_view.GoogleOAuth2Adapter
    callback_url = GOOGLE_CALLBACK_URI
    client_class = OAuth2Client