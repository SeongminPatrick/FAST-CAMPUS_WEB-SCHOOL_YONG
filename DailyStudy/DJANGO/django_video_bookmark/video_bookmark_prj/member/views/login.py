from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login as auth_login,\
    authenticate as auth_authenticate


def login(request):
    next = request.GET.get('next')

    if request.method == 'POST':
        try:
            email = request.POST['email']
            password = request.POST['password']
        except KeyError:
            return messages.error(request, 'email과 password는 필수 요소 입니다.')

        user = auth_authenticate(username=email, password=password)

        if user is not None:
            auth_login(request, user)
            messages.success(request, '로그인에 성공하였습니다')
            return redirect(next)
        else:
            messages.error(request, '로그인에 실패 하였습니다')
            return render(request, 'member/login.html', {})
    else:
        return render(request, 'member/login.html', {})

