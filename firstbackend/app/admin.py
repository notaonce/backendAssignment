from django.contrib import admin
from .models import Post, UserData, Major1, Major2, MajorAdvance, Category, Comment, Like

# Register your models here.

admin.site.register(Post)
admin.site.register(UserData)
admin.site.register(Major1)
admin.site.register(Major2)
admin.site.register(MajorAdvance)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Like)



