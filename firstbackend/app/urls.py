from readline import append_history_file
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from firstbackend.app.models import Post
from . import views
from .views import PostListAPIView, PostDetailAPIView

router = DefaultRouter()
router.register('post', views.PostViewSet) 

app_name = 'app'


urlpatterns = [
    path('posts/', PostListAPIView.as_view()),
    path('posts/<int:pk>/', PostDetailAPIView.as_view()),
    path('', include(router.urls)),

] 