from enum import auto
from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import PROTECT

class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=PROTECT)
    date_create = models.DateField(auto_now_add=True)
    photo = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title
    class Meta:
        ordering = ['date_create']
