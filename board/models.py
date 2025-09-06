from django.db import models
from django.shortcuts import render, redirect

# Create your models here.
class Post(models.Model):
    name = models.CharField(max_length=30)
    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name