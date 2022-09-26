from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# 1. 게시글 및 댓글에 대한 CRUD
# 2. 게시글은 카테고리로 구분 / 카테고리 이름 혹은 카테고리 코드로
# 3. 사용자 정보 관리, 로그인한 사용자만이 게시글 및 댓글 작성
# 4. 사용자 정보로는 사용자 이름, 아이디, 비번, 전공 관리
# 5. 본전공 이외에 이중, 복수, 융합, 심화 정보
# 6. 로그인한 사용자 게시글에는 좋아요 표시 해제할 수 있어야 하며 
# 게시글에는 좋아요를 누른 사용자 수 표시 요구
class MajorAdvance(models.Model) :
    majoradvance = models.CharField(max_length = 16)

class Major1(models.Model) :
    major = models.CharField(max_length = 16)

class Major2(models.Model) : 
    major = models.CharField(max_length = 16)

class Category(models.Model) : 
    category = models.CharField(max_length = 16)
    code = models.CharField(max_length=16, default=None)

class Post(models.Model) :
    title = models.CharField(max_length = 100)
    content = models.TextField()
    category = models.ManyToManyField('Category', related_name = 'posts')
    user = models.ManyToManyField(User, related_name='posts')
    
    def __str__(self):
        return self.title

class UserData(models.Model) :
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=16)
    majoradvance = models.ForeignKey(
        MajorAdvance, on_delete=models.CASCADE, related_name='users'
    )
    major1 = models.ManyToManyField('Major1', related_name = 'users')
    major2 = models.ManyToManyField('Major2', related_name = 'users')
    def __str__(self):
        return self.name

class Comment(models.Model) :
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments'
    )
    comment = models.TextField()
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments'
    )
    def __str__(self):
        return self.comment

class Like(models.Model) :
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name = 'likes'
    )
    user = models.OneToOneField(User, related_name='like', on_delete=models.CASCADE, default=None)
    count = models.IntegerField(default = 0)
