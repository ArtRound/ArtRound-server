from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import GetInfo, ReviewList, ReviewDetail
from .views import QuestionList, QuestionDetail
from .views import AnswerList, AnswerDetail
from .views import NoticeList, NoticeDetail
from .views import FavoritesList, FavoritesDetail
from .views import ArtInfoList, ArtInfoDetail
from .views import VisitedList, VisitedDetail
from .views import KakaoLogin, GoogleLogin
from .views import AddInfo
from main import views

urlpatterns = [
    # path('hello/', helloAPI),
    # path('<int:id>/', create),
    
    path('question/', QuestionList.as_view()),
    path('question/<int:pk>/', QuestionDetail.as_view()),
    
    path('answer/', AnswerList.as_view()),
    path('answer/<int:pk>/', AnswerDetail.as_view()),
    
    path('notice/', NoticeList.as_view()),
    path('notice/<int:pk>/', NoticeDetail.as_view()),
    
    path('favorites/', FavoritesList.as_view()),
    path('favorites/<int:pk>', FavoritesDetail.as_view()),
    
    path('art_info/', ArtInfoList.as_view()), # 전시회들
    path('art_info/<int:pk>', ArtInfoDetail.as_view()), # 전시회 정보
    path('art_info/<int:pk>/favorites', FavoritesList.as_view()), # 즐겨찾기 등록
    path('art_info/<int:pk>/review/', ReviewList.as_view()), # 전시회 리뷰
    path('art_info/<int:pk>/review/<int:pk2>/', ReviewDetail.as_view()), # 전시회 리뷰 디테일
    
    
    path('visited/', VisitedList.as_view()),
    path('visited/<int:pk>', VisitedDetail.as_view()),

    path('login/kakao/', views.kakao_login, name='kakao_login'),
    path('login/kakao/finish/', KakaoLogin.as_view(), name='kakao_login_todjango'),

    path('login/google', views.google_login, name='google_login'),
    path('login/google/finish/', GoogleLogin.as_view(), name='google_login_todjango'),
    
    path('add_info/', AddInfo.as_view(), name='add_info'),
    path('get_info/<int:pk>/', GetInfo.as_view(), name='get_info')
]

urlpatterns = format_suffix_patterns(urlpatterns)
