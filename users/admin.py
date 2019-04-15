from django.contrib import admin
from .models import User,Tools,Logs

# Register your models here.
admin.site.register(User)
admin.site.register(Tools)
admin.site.register(Logs)
