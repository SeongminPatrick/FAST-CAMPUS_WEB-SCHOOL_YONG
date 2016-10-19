from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from oauth2client.tools import argparser
from video.models import Video


DEVELOPER_KEY = "AIzaSyDiarbwPOxSkXmNPfdv8UtHcZM6KySpk34"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"


def youtube_search(keyword, page_token, max_results=10):
    """
    youtube_search함수 개선

    1. youtube_search 함수의 arguments에 pageToken 추가
    2. 받은 pageToken값을 youtube.search()실행 시 list의 인자로 추가
    3. search뷰에서 request.GET에 pageToken값을 받아오도록 설정
    4. template에서 이전페이지/다음페이지 a태그 href에 GET parameter가 추가되도록 설정
    """
    youtube = build(
        YOUTUBE_API_SERVICE_NAME,
        YOUTUBE_API_VERSION,
        developerKey=DEVELOPER_KEY
    )

    search_response = youtube.search().list(
        q=keyword,
        part="id,snippet",
        maxResults=max_results,
        pageToken=page_token
    ).execute()

    video_id_list = []
    for item in search_response['items']:
        if item['id'].get('videoId'):
            video_id_list.append(item['id']['videoId'])

    video_response = youtube.videos().list(
        part="id,snippet,statistics,contentDetails",
        id=",".join(video_id_list)
    ).execute()

    # for item in video_response['items']:
    #     print(item['id'])

    # video.search 뷰에서
    # search_response의 items를 반복하며
    # 반복하고있는 item의 'videoId'값이 이미 갖고있는 Video인스턴스의 youtube_id에 해당하는지 파악
    # 이미 Video인스턴스에 존재하는 video_id일 경우, is_exist에 True대입
    # for item in search_response['items']:
    #     cur_video_id = item['id']['videoId']
    #     if Video.objects.filter(youtube_id=cur_video_id).exists():
    #        item['is_exist'] = True

    # 매 item마다 모든 Video 인스턴스를 검색하지 않고,
    # 모든 item의 video_id값 리스트(video_id_list)를 이용해서
    # 현재 검색결과에 해당하는 Video인스턴스 리스트를 미리 계산(exist_list)
    # 그리고 해당 Video인스턴스 리스트에서 video_id값만 리스트로 빼서 (exist_id_list)
    # items를 forloop하며 video_id값이 검색결과에 해당하는 exist_id_list에 포함되는지 검사해서 is_exist를 True대입
    video_id_list = [item['id'] for item in video_response['items']] #검색된 video리스트
    exist_list = Video.objects.filter(youtube_id__in=video_id_list) #북마크 video중 검색된 video 리스트에 포함된 리스트
    exist_id_list = [video.youtube_id for video in exist_list] # 검색된 video중 북마크에 존재하는 것
    for item in video_response['items']: # 검색된 video중 북마크에 존재하는 것 표시
        cur_video_id = item['id']
        if cur_video_id in exist_id_list:
            item['is_exist'] = True

    video_response['nextPageToken'] = search_response.get('nextPageToken')
    video_response['prevPageToken'] = search_response.get('prevPageToken')
    video_response['pageInfo']['totalResults'] = search_response['pageInfo']['totalResults']

    return video_response
