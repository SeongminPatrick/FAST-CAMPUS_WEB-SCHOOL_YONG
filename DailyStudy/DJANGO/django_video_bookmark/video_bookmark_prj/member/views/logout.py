from django.contrib.auth import logout as auth_logout
from django.contrib import messages
from django.shortcuts import redirect


def logout(request):
    auth_logout(request)
    messages.info(request, '로그아웃 되었습니다.')
    return redirect('video:category_list')