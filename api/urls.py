from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('questions/', views.QuestionList.as_view(), name='question-list'),
    path('questions/<int:pk>/', views.QuestionDetail.as_view(),
         name='question-detail'),
    path('answers/', views.AnswerList.as_view(), name='answer-list'),
    path('users/', views.UserList.as_view(), name='user-list'),
]

urlpatterns += format_suffix_patterns(urlpatterns)
