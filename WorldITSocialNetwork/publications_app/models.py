# from django.db import models
# from django.conf import settings
# # MAX_COMPRESSED_IMAGE_SIZE = 5 * 1024 * 1024

# # Create your models here.

# class Post(models.Model):
#     title = models.CharField(max_length= 255)
#     topic = models.CharField(max_length= 150, null= True )
#     content = models.TextField()
#     created_at = models.DateTimeField(auto_now_add= True )
#     updated_at = models.DateTimeField(auto_now= True)
#     author = models.ForeignKey(to= settings.AUTH_USER_MODEL, on_delete= models.CASCADE)
#     tags = models.ManyToManyField(to= "Tag")
    
# class Tag(models.Model):
#     tag = models.CharField(max_length=100)

# class PostView(models.Model):
#     user = models.ForeignKey(to= settings.AUTH_USER_MODEL, on_delete= models.CASCADE)
#     post = models.ForeignKey(to= settings.AUTH_USER_MODEL, on_delete= models.CASCADE)

# class PostLink(models.Model):
#     url = models.URLField()
#     post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name = "link")
#
# class PostImage():
#   # from django.db import models
# from django.conf import settings
# # MAX_COMPRESSED_IMAGE_SIZE = 5 * 1024 * 1024

# # Create your models here.

# class Post(models.Model):
#     title = models.CharField(max_length= 255)
#     topic = models.CharField(max_length= 150, null= True )
#     content = models.TextField()
#     created_at = models.DateTimeField(auto_now_add= True )
#     updated_at = models.DateTimeField(auto_now= True)
#     author = models.ForeignKey(to= settings.AUTH_USER_MODEL, on_delete= models.CASCADE)
#     tags = models.ManyToManyField(to= "Tag")
    
# class Tag(models.Model):
#     tag = models.CharField(max_length=100)

# class PostView(models.Model):
#     user = models.ForeignKey(to= settings.AUTH_USER_MODEL, on_delete= models.CASCADE)
#     post = models.ForeignKey(to= settings.AUTH_USER_MODEL, on_delete= models.CASCADE)

# class PostLink(models.Model):
#     url = models.URLField()
#     post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name = "link")
#
# class PostImage():
#     