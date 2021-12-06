from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ReviewList, ReviewDetail
from .views import QuestionList, QuestionDetail
from .views import AnswerList, AnswerDetail
from .views import NoticeList, NoticeDetail
from .views import FavoritesList, FavoritesDetail
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
    path('login/kakao/callback', views.kakao_callback, name='kakao_callback'),
    path('login/kakao/finish/', views.KakaoLogin.as_view(), name='kakao_login_todjango'),

    path('login/google', views.google_login, name='google_login'),
    path('login/google/callback', views.google_callback,      name='google_callback'),  
    path('login/google/finish/', views.GoogleLogin.as_view(), name='google_login_todjango'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
