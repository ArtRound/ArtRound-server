from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404, HttpResponse
from django.db.models import Count
from dotenv import load_dotenv
import os, requests, json, jwt

import requests
import urllib.request
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

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import AllowAny

from .serializers import ReviewSerializer, ImageSerializer, QuestionSerializer, AnswerSerializer, NoticeSerializer, FavoritesSerializer, ArtInfoSerializer, UserSerializer, VisitedSerializer
from .models import Review, Image, Question, Answer, Notice, Favorites, ArtInfo, User, Visited

from .forms import ReviewForm

class ReviewList(APIView):
    # 블로그 목록 보여줄 때
    def get(self, request, pk):
        reviews = Review.objects.filter(art_info_id = pk)
        # 여러개 객체 serialize하려면 many=True
        # TO JSON Format
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)

    # 새 글 작성시
    def post(self, request, pk):
        if request.method == 'POST':
            ReviewData = {
                'title' : request.POST.get('title'),
                'content' : request.POST.get('content'),
                'user_id' : request.POST.get('user_id'),
                'heart' : request.POST.get('heart'),
                'art_info_id' : pk
            }
            form = ReviewForm(ReviewData)
            
            if form.is_valid():
                review = form.save()
                image_list = request.FILES.getlist('image')
                for item in image_list: 
                    images = Image.objects.create(review_id=review.id, image=item)
                    images.save()
                return Response(form.data, status=status.HTTP_201_CREATED)
            return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)


class ReviewDetail(APIView):
    # Review 객체 가져오기
    def get_object(self, pk2):
        try:
            return Review.objects.filter(pk=pk2)
        except Review.DoesNotExist:
            raise Http404
        
    # Review detail 보기
    def get(self, request, pk, pk2, format=None):
        review = self.get_object(pk2)
        serializer = ReviewSerializer(review, many=True)
        
        return Response(serializer.data)

    # Review 수정하기
    def put(self, request, pk, pk2, format=None):
        review = self.get_object(pk2)
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid():  # 유효성 검사
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Review 삭제하기
    def delete(self, request, pk, pk2, format=None):
        review = self.get_object(pk2)
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
    def get(self, request, pk):
        favorites = Favorites.objects.all()
        favorites = favorites.filter(user_id=pk)
        
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

def get_art_info():
        data = []
        idx = 0
        for i in range(1,17):
            url = "http://api.data.go.kr/openapi/tn_pubr_public_museum_artgr_info_api?serviceKey=BfdusobQEjVcCsm1nVfc3AnA%2BsBih1Corc0TwKt9B%2Ft46CeONaFq%2Bn0%2BxkUnGO9fzeQHPLjXLLCk8aFpYejEbQ%3D%3D&pageNo="+str(i)+"&numOfRows=100&type=json"
            art_api_request = urllib.request.Request(url)
            response = urllib.request.urlopen(art_api_request)
            rescode = response.getcode()

            if (rescode == 200):
                response_body = response.read()
                result = json.loads(response_body.decode('utf-8'))
                items = result.get('response')['body']['items']

                for i in range(len(items)):
                    items[i]['id'] = idx
                    data.append(items[i])
                    ArtInfo.objects.create(id=items[i]['id'], fcltyNm=items[i]['fcltyNm'],
                                           weekdayOperOpenHhmm=items[i]['weekdayOperOpenHhmm'], 
                                           weekdayOperColseHhmm=items[i]['weekdayOperColseHhmm'],
                                           holidayOperOpenHhmm=items[i]['holidayOperOpenHhmm'], 
                                           holidayCloseOpenHhmm=items[i]['holidayCloseOpenHhmm'],
                                           rstdeInfo=items[i]['rstdeInfo'], adultChrge=items[i]['adultChrge'],
                                           yngbgsChrge=items[i]['yngbgsChrge'], childChrge=items[i]['childChrge'], 
                                           rdnmadr=items[i]['rdnmadr'], phoneNumber=items[i]['phoneNumber'], 
                                           homepageUrl=items[i]['homepageUrl'], latitude=items[i]['latitude'], longitude=items[i]['longitude']
                                           )
                    idx+=1
                    
class ArtInfoList(APIView):
    def get(self, request):
        art_info = ArtInfo.objects.all()
        if(len(art_info)==0):
            get_art_info()
            art_info = ArtInfo.objects.all()
        serializer = ArtInfoSerializer(art_info, many=True)
        
        return Response(serializer.data)

class ArtInfoDetail(APIView):
    # ArtInfo 객체 가져오기
    def get_object(self, pk):
        try:
            return ArtInfo.objects.get(pk=pk)
        except ArtInfo.DoesNotExist:
            raise Http404

    # ArtInfo Read
    def get(self, request, pk, format=None):
        art_info = self.get_object(pk)
        serializer = ArtInfoSerializer(art_info)
        return Response(serializer.data) 
    
#--------------------------------------------------------------------------------

class VisitedList(APIView):
    # 방문 목록
    def get(self, request, pk):
        visited = Visited.objects.all()
        visited = visited.filter(user_id=pk)

        serializer = VisitedSerializer(visited, many=True)
        return Response(serializer.data)

    # Visited Create
    def post(self, request):
        serializer = VisitedSerializer(data=request.data)  # request.data : 사용자 입력 데이터
        if serializer.is_valid():  # 유효성 검사
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VisitedDetail(APIView):
    # Visited 객체 가져오기
    def get_object(self, pk):
        try:
            return Visited.objects.get(pk=pk)
        except Visited.DoesNotExist:
            raise Http404

    # Visited Read
    def get(self, request, pk, format=None):
        visited = self.get_object(pk)
        serializer = VisitedSerializer(visited)
        return Response(serializer.data)

    # Visited Delete
    def delete(self, request, pk, format=None):
        visited = self.get_object(pk)
        visited.delete()
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
        print(kakao_response['kakao_account']['profile'])

        # 새로 가입했을 때
        if not User.objects.filter(id = kakao_response['id']).exists():
            print('새로 가입')
            user = User.objects.create(
                id = kakao_response['id'],
                profile_image = kakao_response['kakao_account']['profile']['profile_image_url']
            )
            q = User.objects.annotate(Count("id"))
            print(q.count())      
                
            jwt_token = jwt.encode({'id':kakao_response['id']}, SECRET_KEY, ALGORITHM)
            print(jwt_token, type(jwt_token))
            if type(jwt_token) is bytes : 
                jwt_token = jwt_token.decode('utf-8')
                print(jwt_token, "fixed")
            # res = JsonResponse({"result":"false","id":kakao_response["id"],"email":kakao_response['kakao_account'].get('email',None),})
            res = JsonResponse({"existing_user":"false",
                                "id":kakao_response["id"], "profile_image":kakao_response['kakao_account']['profile']['profile_image_url'], 
                                "name": None, "age":0, "gender":None})

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
            
            user = User.objects.get(id = kakao_response['id'])
            
            jwt_token = jwt.encode({'id':kakao_response['id']}, SECRET_KEY, ALGORITHM)
            print(jwt_token,type(jwt_token))
            if type(jwt_token) is bytes : 
                jwt_token = jwt_token.decode('utf-8')
                print(jwt_token,"fixed")
            
            res = JsonResponse({"existing_user":"true", "jwt_token": jwt_token, 
                                "id":kakao_response["id"],  "profile_image":kakao_response['kakao_account']['profile']['profile_image_url'], 
                                "name": user.id, "age":user.age, "gender":user.gender})
            res["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
            res["Access-Control-Allow-Credentials"]="true"
            # res["Access-Control-Allow-Origin"] = "https://1n1n.io"
            res["Acess-Control-Max-Age"] = "1000"
            res["Access-Control-Allow-Headers"] = "X-Requested-With, Origin, X-Csrftoken, Content-Type, Accept"
            res.set_cookie(key="jwt_token", value=jwt_token, samesite=None, httponly=True, secure=True)
            return res    

#--------------------------------------------------------------------------------

GOOGLE_CALLBACK_URI = 'http://localhost:3000/main/login/google'
state = "a9dfjGJwkAQek3G"

def google_login(request):
    # Code Request
    scope = "https://www.googleapis.com/auth/userinfo.email"
    client_id = getattr(settings, "SOCIAL_AUTH_GOOGLE_CLIENT_ID")
    return redirect(f"https://accounts.google.com/o/oauth2/v2/auth?client_id={client_id}&response_type=code&redirect_uri={GOOGLE_CALLBACK_URI}&scope={scope}")

class GoogleLogin(SocialLoginView):
    adapter_class = google_view.GoogleOAuth2Adapter
    callback_url = GOOGLE_CALLBACK_URI
    client_class = OAuth2Client
    
    def post(self, request):
        load_dotenv(verbose=True)
        SECRET_KEY = os.getenv("SECRET_KEY")
        ALGORITHM = os.getenv("ALGORITHM")
        
        access_token = json.loads(request.body)
        print(access_token)
        
        google_id = access_token["params"]["code"]["profileObj"]["googleId"]
        google_name = access_token["params"]["code"]["profileObj"]["name"]
        google_email = access_token["params"]["code"]["profileObj"]["email"]
        print(google_email, google_name, google_id)
        
        # 새로 가입했을 때
        if not User.objects.filter(id = google_id).exists():
            user = User.objects.create(
                id = google_id,
            )
            jwt_token = jwt.encode({'id':google_id}, SECRET_KEY, ALGORITHM)
            print(jwt_token)
            
            res = HttpResponse({"success":True})
            res.set_cookie(key="access_token", value=jwt_token, httponly=True, secure=True)
            
            return res
        
        # 이미 가입되어있을 때
        else:     
            user = User.objects.get(id = google_id)
            jwt_token = jwt.encode({'id':user.id}, SECRET_KEY, ALGORITHM)
            print(jwt_token)
            
            res = HttpResponse({"success":True})
            res.set_cookie(key="access_token", value=jwt_token, httponly=True, secure=True)
            return res       

#--------------------------------------------------------------------------------

class AddInfo(APIView):
    def post(self, request):
        user_info = json.loads(request.body)
        print(user_info)
        user = User.objects.get(id = user_info['params']['id'])
        User(
            id = user_info['params']['id'],
            name = user_info['params']['name'],
            gender = user_info['params']['gender'],
            age = user_info['params']['age'],
            created_at = user.created_at
        ).save()
        
        return JsonResponse({"data":True})

class GetInfo(APIView):
    def get(self, request, pk):
        user = User.objects.filter(pk=pk)
        print('여기는 GetInfo')
        print(pk)
        serializer = UserSerializer(user,many=True)
        return Response(serializer.data)