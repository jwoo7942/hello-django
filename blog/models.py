from django.db import models
#from django.contrib.auth.models import User
from django.conf import settings

#settings.AUTH_USER_MODEL


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, db_index=True)
    content = models.TextField()
    tags = models.CharField(max_length=20)
    is_publish = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    #post의 title을 post_object가 아니라 실제 post의 title을 보여주게 된다.
    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author_name = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


"""
class ZipCode(models.Model):
    # code = models.CharField(max_length=6, primary_key=True)
    code = models.CharField(max_length=6, unique=True)
    desc = models.TextField()
"""