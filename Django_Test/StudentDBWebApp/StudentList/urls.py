from django.urls import path
from . import views
from django.conf.urls import  url

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url('testing/', views.newpage, name='new'),
    url(r'^(?P<stud_id>[0-9]+)/$', views.studlist, name ='studlist')
]
