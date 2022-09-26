from unicodedata import category
from django.shortcuts import render, redirect
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
from django.shortcuts import get_object_or_404



# Create your views here.

class PostListAPIView(APIView) : 
    serializer_class = PostSerializer
    def get_seri(self, *args, **kwargs) :
        serializer = PostSerializer
        kwargs['context'] = {'reqeust' : self.request}
        return serializer(*args, **kwargs)

    def get(self, request) :
        code = request.data['code']
        category = Category.objects.get(code=code)
        filtered = Post.objects.filter(category=category)
        postserializer = self.get_seri(filtered, many=True)
        return Response(postserializer.data, category, status = status.HTTP_200_OK)

    def post(self, request) : 
        data = {}
        data['title'] = request.data['title']
        data['content'] =  request.data['content']
        code = request.data['code']
        data['category'] = Category.objects.get(code=code).category
        serializer = self.get_seri(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PostDetailAPIView(APIView) :
    serializer_class = PostSerializer
    def get_object(self, pk):
        return get_object_or_404(Post, pk=pk)
    def get(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)
    def put(self, request, pk) : 
        post = self.get_object(pk)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        post = self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ToggleLikeAPIView(APIView):
    def get(self, request, post_pk):
        post = Post.objects.get(pk=post_pk)
        serializer = PostSerializer
        return Response(serializer.data, status=status.HTTP_200_OK)
        



        

def login(request) :
    if request.method == 'POST':
        found_user = User.objects.filter(username=request.POST['username'])
        if (len(found_user) > 0):
            error = 'username이 이미 존재합니다'
            return render(request, 'signup.html', {'error': error})

        new_user = User.objects.create(
            userid=request.POST['userid'],
            password=request.POST['password'],
            name=request.POST['name'],
            majoradvance=request.POST['majoradvance'],
            major1=request.POST['major1'],
            major2=request.POST['major2'],
        )
        auth.login(
            request,
            new_user,
            backend='django.contrib.auth.backends.ModelBackend'
        )
        return redirect('home')
        
    return render(request, 'login.html')

def signup(request) :
    if request.method == 'POST':
        found_user = User.objects.filter(username=request.POST['username'])
        if (len(found_user) > 0):
            error = 'username이 이미 존재합니다'
            return render(request, 'signup.html', {'error': error})

        new_user = User.objects.create(
            userid=request.POST['userid'],
            password=request.POST['password'],
            name=request.POST['name'],
            majoradvance=request.POST['majoradvance'],
            major1=request.POST['major1'],
            major2=request.POST['major2'],
        )
        auth.login(
            request,
            new_user,
            backend='django.contrib.auth.backends.ModelBackend'
        )
        return redirect('home')
    return render(request, 'signup.html')
