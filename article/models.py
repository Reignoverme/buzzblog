from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# import MySQLdb


class Tag(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=100)


class Post(models.Model):
    def __str__(self):
        return self.title

    title = models.CharField(max_length=70)
    body = models.TextField()
    created_time = models.DateTimeField()
    tags = models.ManyToManyField(Tag, blank=True)
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE)

    def get_abs_url(self):
        # 每篇文章通过调用这个方法自动生成URL
        return reverse('article:read', kwargs={'title': self.title})
