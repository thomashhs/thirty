from django.conf.urls import url
from . import views

urlpatterns = [
    # ex : /polls/
    url(r'^register/$', views.register, name='register'),
    url(r'^index/$', views.index, name='index'),
    url(r'^tools/$', views.tools, name='tools'),
    url(r'^tools/(?P<tool_name>\w+)/$', views.toolname, name='toolname'),
    url(r'^about/$', views.about, name='about'),

]