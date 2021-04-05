from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('', views.Search.as_view()),
    path('questions/', views.QuestionList.as_view(), name='question-list'),
    path('questions/<int:pk>/', views.QuestionDetail.as_view(),
        name='question-detail'),
    path('answers/', views.AnswerList.as_view(), name='answer-list'),
    path('answers/<int:pk>/', views.AnswerDetail.as_view(), 
        name='answer-detail'),
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), 
        name='user-detail'),
]

urlpatterns += format_suffix_patterns(urlpatterns)
