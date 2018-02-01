from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from faker import Faker
import MySQLdb


# class Article(models.Model):
#     title = models.CharField(max_length=100)  # 博客题目
#     category = models.CharField(max_length=50, blank=True)  # 博客标签
#     date_time = models.DateTimeField(auto_now_add=True)  # 博客日期
#     content = models.TextField(blank=True, null=True)  # 博客文章正文

#     # python2使用__unicode__, python3使用__str__
#     def __str__(self):
#         return self.title

#     class Meta:  # 按时间下降排序
#         ordering = ['-date_time']

# class Category(models.Model):
#     name = models.CharField(max_length=100)


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

    def test_data(self):
        fake = Faker()
        db = MySQLdb.connect(host='localhost', user='root',
                             password='grinee123', db='testblog')
        x = db.cursor()

        for i in range(6, 17):
            try:
                x.execute("INSERT INTO article_post VALUES(%s, %s, %s, %s, %s)",
                          (i, fake.name(), fake.text(),
                           fake.date() + ' ' + fake.time(),
                           1))
                db.commit()
            except:
                db.rollback()
        db.close()
