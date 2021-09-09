from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ReviewList, ReviewDetail
from .views import QuestionList, QuestionDetail
from .views import NoticeList, NoticeDetail

urlpatterns = [
    # path('hello/', helloAPI),
    # path('<int:id>/', create),
    path('review/', ReviewList.as_view()),
    path('review/<int:pk>/', ReviewDetail.as_view()),
    path('question/', QuestionList.as_view()),
    path('question/<int:pk>/', QuestionDetail.as_view()),
    path('notice/', NoticeList.as_view()),
    path('notice/<int:pk>/', NoticeDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
