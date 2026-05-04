from django.db import models
from django.conf import settings


class Post(models.Model):
    title = models.CharField(max_length=255)
    topic = models.CharField(
        max_length=150,
        null=True
    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    tag = models.ManyToManyField(
        'Tag',
        blank=True
    )

class Tag(models.Model):
    name = models.CharField(max_length=100)

class PostImage(models.Model):
    original_image = models.ImageField(upload_to='post_app/images')
    compressed_image = models.ImageField(upload_to = 'post_app/images')
    post = models.ForeignKey(
        Post, 
        on_delete=models.CASCADE
    )