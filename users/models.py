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