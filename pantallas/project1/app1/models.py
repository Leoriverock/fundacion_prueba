from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    imagen = models.ImageField(upload_to="posts", null=True)