from django.urls import include, path
from .views import PostListAPIView, PostDetailAPIView, CommentAPIView, ToggleLikeAPIView

app_name = 'app'
urlpatterns = [
    path('posts/', PostListAPIView.as_view()),
    path('posts/<int:pk>/', PostDetailAPIView.as_view()),
] 

#하나의 url에 여러 개의 view를 넣는 방법 탐색해보기