from django.urls import path
from .views import ReviewList, ReviewDetail

urlpatterns = [
    # path('hello/', helloAPI),
    # path('<int:id>/', create),
    path('ReviewList/', ReviewList.as_view()),
]
