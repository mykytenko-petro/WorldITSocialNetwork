from django.db import models

# Create your models here.

class ModalPublication(models.Model):
    title = models.CharField()
    topic = models.CharField()
    
class Tag():
    tag = models.