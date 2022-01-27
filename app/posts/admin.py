from django.contrib import admin
from app.posts.models import Post, Comment

admin.site.register(Post)
admin.site.register(Comment)
