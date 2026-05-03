from django.db import models

# Create your models here.

class PublicationModel(models.Model):
    title = models.CharField()
    topic = models.CharField()
    
class TagModel(models.Model):
    name = models.CharField()
    
    def __str__(self):
        return f"name: {self.name}"
    
class 