from dataclasses import field
from rest_framework import serializers as sz
from .models import Post, UserData, Major1, Major2, MajorAdvance, Category, Comment, Like

class PostSerializer(sz.ModelSerializer) :
    class Meta:
        model = Post
        fields = ('title', 'content', 'category')

class UserDataSerializer(sz.ModelSerializer) : 
    class Meta :
        model = UserData
        fields = ('user', 'name', 'majoradvance', 'major1', 'major2')


class CommentSerializer(sz.ModelSerializer) : 
    class Meta :
        model = Comment
        fields = ('post', 'commnet', 'author')

class LikeSerializer(sz.ModelSerializer) :
    class Meta :
        model = Like
        fleids = '__all__' 

class CategorySerializer(sz.ModelSerializer) :
    class Meta :
        model = Category
        fleids = '__all__' 