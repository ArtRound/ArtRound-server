from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import GetInfo, ReviewList, ReviewDetail
from .views import QuestionList, QuestionDetail
from .views import AnswerList, AnswerDetail
from .views import NoticeList, NoticeDetail
from .views import FavoritesList, FavoritesDetail
from .views import KakaoLogin, GoogleLogin
from .views import AddInfo
from main import views

urlpatterns = [
    # path('hello/', helloAPI),
    # path('<int:id>/', create),
    path('review/', ReviewList.as_view()),
    path('review/<int:pk>/', ReviewDetail.as_view()),
    path('question/', QuestionList.as_view()),
    path('question/<int:pk>/', QuestionDetail.as_view()),
    path('answer/', AnswerList.as_view()),
    path('answer/<int:pk>/', AnswerDetail.as_view()),
    path('notice/', NoticeList.as_view()),
    path('notice/<int:pk>/', NoticeDetail.as_view()),
    path('favorites/', FavoritesList.as_view()),
    path('favorites/<int:pk>', FavoritesDetail.as_view()),

    path('login/kakao/', views.kakao_login, name='kakao_login'),
    path('login/kakao/finish/', KakaoLogin.as_view(), name='kakao_login_todjango'),

    path('login/google', views.google_login, name='google_login'),
    path('login/google/finish/', GoogleLogin.as_view(), name='google_login_todjango'),
    
    path('add_info/', AddInfo.as_view(), name='add_info'),
    path('get_info/<int:pk>/', GetInfo.as_view(), name='get_info')
]

urlpatterns = format_suffix_patterns(urlpatterns)
