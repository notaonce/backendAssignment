from django.urls import include, path
from .views import PostListAPIView, PostDetailAPIView

app_name = 'app'
urlpatterns = [
    path('posts/', PostListAPIView.as_view()),
    path('posts/<int:pk>/', PostDetailAPIView.as_view()),
] 