from django.db import models
from django.conf import settings
from PIL import Image


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
    tags = models.ManyToManyField(
        'Tag',
        blank=True
    )

    def __str__(self) -> str:
        return self.title

class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name

class PostImage(models.Model):
    original_image = models.ImageField(upload_to='post_app/images')
    compressed_image = models.ImageField(upload_to='post_app/images')
    post = models.ForeignKey(
        Post, 
        on_delete=models.CASCADE,
        related_name="images"
    )

    def __str__(self) -> str:
        return self.original_image.name
    
    # known issue: if it will be moved to cloud storage it would break
    # solution is make width and height fields later
    @property
    def orientation(self):
        with Image.open(self.compressed_image.path) as img:
            if img.width > img.height:
                return "landscape"
            
            elif img.height >= img.width:
                return "portrait"


class PostView(models.Model):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(to=Post, on_delete= models.CASCADE)

class PostLink(models.Model):
    url = models.URLField()
    post = models.ForeignKey(
        to=Post,
        on_delete=models.CASCADE,
        related_name="links"
    )
