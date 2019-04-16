from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    nickname = models.CharField(max_length=50, blank=True)

    class Meta(AbstractUser.Meta):
        pass

class Tools(models.Model):
    name = models.CharField(primary_key=True,max_length=128)
    title = models.CharField(max_length=254)
    desc = models.CharField(max_length=254)
    visible = models.BooleanField()
    date_add = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Logs(models.Model):
    title = models.CharField(max_length=254)
    pub_date = models.DateTimeField(auto_now_add=True)
    desc = models.TextField()
    is_visible = models.BooleanField()
    is_left = models.BooleanField()

    def __str__(self):
        return self.title

#文章分类
class Category(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name

#文章标签
class Tag(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name

#博客文章
class Post(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    created_time=models.DateTimeField()
    modified_time=models.DateTimeField()
    excerpt=models.CharField(max_length=200,blank=True)
    category=models.ForeignKey(Category)
    tags=models.ManyToManyField(Tag,blank=True)
    author=models.ForeignKey(User)
    #新增字段统计阅读量
    views=models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    def increase_views(self):
        self.views+=1
        self.save(update_fields=['views'])

    class Meta:
        ordering=['-created_time']