"""video_bookmark URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from .views import video_list, video_detail, video_new, video_like,\
                    category_list, category_edit, category_delete

urlpatterns = [
    url(r'category/$', category_list, name="category_list"),
    url(r'category/(?P<pk>[0-9]+)/edit/$', category_edit, name="category_edit"),
    url(r'category/(?P<pk>[0-9]+)/delete/$', category_delete, name="category_delete"),


    url(r'^list/(?P<pk>[0-9]+)/$', video_list, name="video_list"),
    url(r'^(?P<pk>[0-9]+)/$', video_detail, name="video_detail"),
    url(r'^(?P<pk>[0-9]+)/like/$', video_like, name="video_like"),
    url(r'^new/$', video_new, name="video_new"),
]
