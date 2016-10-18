from django.shortcuts import render, HttpResponse, redirect
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from oauth2client.tools import argparser
from .models import Video

DEVELOPER_KEY = "AIzaSyDiarbwPOxSkXmNPfdv8UtHcZM6KySpk34"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"


def youtube_search(keyword, page_token, max_results=10):
    youtube = build(
        YOUTUBE_API_SERVICE_NAME,
        YOUTUBE_API_VERSION,
        developerKey=DEVELOPER_KEY
    )

    search_response = youtube.search().list(
        q=keyword,
        part="id,snippet",
        maxResults=max_results,
        pageToken=page_token,
    ).execute()

    return search_response


def search(request):
    context = {}
    keyword = request.GET.get('keyword')
    page_token = request.GET.get('page_token')
    if keyword:
        response = youtube_search(keyword, page_token)
        context['keyword'] = keyword
        context['response'] = response
    return render(request, 'video/search.html', context)


def add_bookmark(request):
    next = request.GET.get('next')
    kind = request.POST.get('kind')
    youtube_id = request.POST.get('youtube_id')
    title = request.POST.get('title')
    description = request.POST.get('description')
    published_date = request.POST.get('published_date')
    thumbnail = request.POST.get('thumbnail')

    Video.objects.create(
        kind=kind,
        youtube_id=youtube_id,
        title=title,
        description=description,
        published_date=published_date,
        thumbnail=thumbnail
    )
    return redirect(next)


def bookmark_list(request):
    videos = Video.objects.all()
    context = {
        'videos': videos
    }
    return render(request, 'video/list.html', context)