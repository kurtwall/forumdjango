from django.db import models
from django.conf import settings


class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(blank=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.CASCADE,
                             related_name="posts")
    created_at = models.DateTimeField(null=True, auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.CASCADE,
                             related_name="comments")
    post = models.ForeignKey(Post, blank=True, null=True, on_delete=models.CASCADE, related_name="comments")
    body = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(null=True, auto_now_add=True)

    def __str__(self):
        return self.body[:10]
