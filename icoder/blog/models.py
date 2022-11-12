from asyncio.windows_events import NULL
from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.
class post(models.Model):
    sno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=50)
    content=models.TextField(max_length=500)
    slug=models.CharField(max_length=20)
    author=models.CharField(max_length=50)
    timestamp=models.DateTimeField()
    views=models.IntegerField(default=0)

    def __str__(self):
        return self.title + " by " +self.author


class comment(models.Model):
    blogsno=models.AutoField(primary_key=True)
    blogcomment=models.TextField()
    bloguser=models.ForeignKey(User,on_delete=models.CASCADE)
    blogpost=models.ForeignKey(post,on_delete=models.CASCADE)
    blogparent=models.ForeignKey('self',on_delete=models.CASCADE,null=True,blank=True)
    blogtimestamp=models.DateTimeField(default=now)

    def __str__(self):
        return self.blogcomment + " by " + self.bloguser.username