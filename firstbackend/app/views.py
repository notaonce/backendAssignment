from platform import libc_ver
from re import L
from .models import Post, UserData, Major1, Major2, MajorAdvance, Category, Comment, Like
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .serializers import PostSerializer, UserDataSerializer, CommentSerializer, LikeSerializer, CategorySerializer
from rest_framework import viewsets
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404, get_list_or_404



# Create your views here.

class PostListAPIView(APIView) : 
    serializer_class = PostSerializer
    def get_seri(self, *args, **kwargs) :
        serializer = PostSerializer
        kwargs['context'] = {'reqeust' : self.request}
        return serializer(*args, **kwargs)

    def get(self, request, catcode) :
        code = catcode
        category = Category.objects.get(code=code)
        filtered = Post.objects.filter(category=category)
        postserializer = self.get_seri(filtered, many=True)
        return Response(postserializer.data, category, status = status.HTTP_200_OK)

    def post(self, request, catcode) : 
        data = {}
        data['title'] = request.data['title']
        data['content'] =  request.data['content']
        code = catcode
        data['category'] = Category.objects.get(code=code).category
        serializer = self.get_seri(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PostDetailAPIView(APIView) :
    serializer_class = PostSerializer
    def get_post(self, pk):
        return get_object_or_404(Post, pk=pk)
    

    def get(self, request, pk, format=None):
        post = self.get_post(pk)
        postserializer = PostSerializer(post)
        return Response(postserializer.data)

    def put(self, request, pk) : 
        post = self.get_post(pk)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        post = self.get_post(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CommentAPIView(APIView) :
    def get_comment_list(self, post_pk) : 
        return get_list_or_404(Comment, post=self.get_post(post_pk))
    
    def get_comment(self, comment_pk) :
        return get_object_or_404(Comment, pk=comment_pk)

    def get(self, request, post_pk, comment_pk) :
        comment = self.get_comment(post_pk)
        commentserializer = CommentSerializer(comment)
        return Response(commentserializer.data)
    
    def post(self, request, post_pk, comment_pk) :
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, post_pk, comment_pk) : 
        comment = self.get_comment(comment_pk)
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, post_pk, comment_pk) : 
        comment = self.get_comment(comment_pk)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ToggleLikeAPIView(APIView):
    def get_like(self, post_pk):
        return get_list_or_404(Like, pk=post_pk)

    def get(self, request, post_pk):
        like = self.get_like(post_pk)
        serializer = LikeSerializer(like)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, post_pk):
        like = self.get_like(post_pk)
        if like :
            #like에서 사용자 찾고 사용자가 누른 like 삭제
            like.delete()
            return Response(status=status.HTTP_204_NO_Content)
        else :
            serializer = LikeSerializer(like, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        



# 구현해야 하는 기능 : 로그인 확인, 카테고리 연동, 유저데이터 모델과 유저 모델 연동
# 목요일까지 최선을 다해보겠습니다...............

        

# def login(request) :
#     if request.method == 'POST':
#         found_user = User.objects.filter(username=request.POST['username'])
#         if (len(found_user) > 0):
#             error = 'username이 이미 존재합니다'
#             return render(request, 'signup.html', {'error': error})

#         new_user = User.objects.create(
#             userid=request.POST['userid'],
#             password=request.POST['password'],
#             name=request.POST['name'],
#             majoradvance=request.POST['majoradvance'],
#             major1=request.POST['major1'],
#             major2=request.POST['major2'],
#         )
#         auth.login(
#             request,
#             new_user,
#             backend='django.contrib.auth.backends.ModelBackend'
#         )
#         return redirect('home')
        
#     return render(request, 'login.html')

# def signup(request) :
#     if request.method == 'POST':
#         found_user = User.objects.filter(username=request.POST['username'])
#         if (len(found_user) > 0):
#             error = 'username이 이미 존재합니다'
#             return render(request, 'signup.html', {'error': error})

#         new_user = User.objects.create(
#             userid=request.POST['userid'],
#             password=request.POST['password'],
#             name=request.POST['name'],
#             majoradvance=request.POST['majoradvance'],
#             major1=request.POST['major1'],
#             major2=request.POST['major2'],
#         )
#         auth.login(
#             request,
#             new_user,
#             backend='django.contrib.auth.backends.ModelBackend'
#         )
#         return redirect('home')
#     return render(request, 'signup.html')
