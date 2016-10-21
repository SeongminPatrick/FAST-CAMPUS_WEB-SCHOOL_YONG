import requests
import json
from django.http import HttpResponse
from django.urls import reverse
from member.apis import facebook
from django.shortcuts import render

__all__ = [
    'friends_ranking'
]


def friends_ranking(request):
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
        url_request_feed = 'https://graph.facebook.com/v2.8/{user_id}/feed?' \
                           'fields=comments&' \
                           'access_token={access_token}'.format(
                            user_id=user_id,
                            access_token=access_token,
                            )

        r = requests.get(url_request_feed)
        dict_feed_info = r.json()
        json_data = json.dumps(dict_feed_info, indent=2)

        temp_custom_data = []
        for feed in dict_feed_info['data']:
            if feed.get('comments'):
                for data in feed.get('comments')['data']:
                    data['from']['message'] = data['message']
                    temp_custom_data.append(data['from'])

        custom_data = []
        for i in temp_custom_data:
            cnt = 0
            temp_message = []
            if not (i['id'] in [i['id'] for i in custom_data]) and (i['id'] != user_id):
                for j in temp_custom_data:
                    if i['id'] == j['id']:
                        temp_message.append(j['message'])
                        cnt += 1
                custom_data.append({
                    'id': i['id'],
                    'name': i['name'],
                    'cnt': cnt,
                    'message': temp_message
                })

        custom_data = sorted(custom_data, key=lambda k: k['cnt'], reverse=True)

        context = {
            'custom_data': custom_data
        }
        return render(request, 'sns/friends_ranking.html', context)
