from django.http import HttpResponse
from django.contrib.auth import authenticate as auth_authenticate, login as auth_login
from django.contrib import messages
from django.shortcuts import render, redirect


def login(request):
    next = request.GET.get('next') #[]는 keyerror가 나오지만 get은 없을 경우에 None이 들어가게 된다.
    if request.method == 'POST':
        try:
            username = request.POST['username']
            password = request.POST['password']
        except KeyError:
            return HttpResponse("username 또는 password는 필수 입니다.")
        user = auth_authenticate( # 인증 부분만 담당한다.
            username=username,
            password=password
        )
        if user is not None:
            auth_login(request, user) # session에 id값을 등록한다. cookey에 id값을 실어서 보내주는것은 middleware가 담당한다.
            messages.success(request, '로그인에 성공하였습니다')# login에서 render로 보내주면 새로고침 해주면 로그인을 다시해야한다?
            return redirect(next) # redirect는 browser밖으로 나갔다가 다시 들어오는것이고 render는 장고내부에서 이동한다.
        else:
            messages.error(request, '로그인에 실패하였습니다')
            return render(request, 'member/login.html', {})
    else:
        return render(request, 'member/login.html', {})
