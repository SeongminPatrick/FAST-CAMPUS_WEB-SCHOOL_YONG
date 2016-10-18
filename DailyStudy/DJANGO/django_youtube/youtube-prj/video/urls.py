from django.conf.urls import url
from video import views

urlpatterns = [
    url(r'^search/$', views.search, name='search'),
    url(r'^add/$', views.add_bookmark, name='add'),
    url(r'^list/$', views.bookmark_list, name='list'),

]
