import requests
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse
from sns.models import FriendsRank
from member.apis import facebook

__all__ = [
    'update_friends_ranking',
    'show_friends_ranking',
    'show_mypost'
]


def update_friends_ranking(request):
    if request.GET.get('error'):
        return HttpResponse('사용자 로그인 거부')
    if request.GET.get('code'):
        redirect_uri = 'http://{host}{url}'.format(
            host=request.META['HTTP_HOST'],
            url=reverse('sns:friends_ranking')
        )
        code = request.GET.get('code')
        access_token = facebook.get_access_token(code, redirect_uri)
        user_id = facebook.get_user_id_from_token(access_token)
        url_request_feed = 'https://graph.facebook.com/v2.8/{user_id}/feed?fields=' \
                           'comments{{from{{name,picture.type(normal)}}}}&' \
                           'access_token={access_token}'.format(
                            user_id=user_id,
                            access_token=access_token,
                            )

        r = requests.get(url_request_feed)
        dict_feed_info = r.json()
        temp_custom_data = []

        while dict_feed_info.get('paging'):
            for feed in dict_feed_info['data']:
                if feed.get('comments'):
                    for data in feed.get('comments')['data']:
                        data['from']['picture_url'] = data['from']['picture']['data']['url']
                        temp_custom_data.append(data['from'])
            url_request_feed = dict_feed_info['paging']['next']
            r = requests.get(url_request_feed)
            dict_feed_info = r.json()

        custom_data = []
        for i in temp_custom_data:
            cnt = 0
            if not (i['id'] in [i['id'] for i in custom_data]) and (i['id'] != user_id):
                for j in temp_custom_data:
                    if i['id'] == j['id']:
                        cnt += 1
                obj, created = FriendsRank.objects.update_or_create(
                    friends_id=i['id'],
                    defaults={
                        'friends_id': i['id'],
                        'name': i['name'],
                        'picture_url': i['picture_url'],
                        'comment_count': cnt,
                    })

        return render(request, 'sns/update_friends_ranking.html', {})


def show_friends_ranking(request):
    friends = FriendsRank.objects.all().order_by('-comment_count')
    context = {
        'friends': friends
    }

    return render(request, 'sns/show_friends_ranking.html', context)


def show_mypost(request):
    if request.GET.get('error'):
        return HttpResponse('사용자 거부')
    if request.GET.get('code'):
        redirect_uri = 'http://{host}{url}'.format(
            host=request.META['HTTP_HOST'],
            url=reverse('sns:show_mypost')
        )
        code = request.GET.get('code')
        access_token = facebook.get_access_token(code, redirect_uri)
        user_id = facebook.get_user_id_from_token(access_token)
        url_request_post = 'https://graph.facebook.com/v2.8/{user_id}/posts?' \
                           'access_token={access_token}'.format(
                            user_id=user_id,
                            access_token=access_token,
                            )
        r = requests.get(url_request_post)
        dict_post_info = r.json()
        print(dict_post_info)

        post_data_list = []
        for post in dict_post_info['data']:
            if post.get('message'):
                post_data_list.append({
                     'message':post['message'],
                     'created_time':post['created_time'],
                    })

        context ={
            'posts': post_data_list,
        }
        return render(request, 'sns/show_my_posts.html', context)
