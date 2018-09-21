from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db.models import Sum
from django.http import HttpResponse
from django.shortcuts import render, redirect
# Create your views here.
from apps.home.models import *


def register_view(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        if User.objects.filter(username=username):
            return render(request, 'register.html', {'msg': '用户已存在'})
        else:
            # 注册用户
            user = User.objects.create_user(username=username, password=password, email=email)
            user_profile = UserProfile(phone=phone, user_id=user.id)
            user_profile.save()
            # 管理员用户
            # User.objects.create_superuser()
            return redirect('/')


# login 协程
def login_view(request):
    if request.method == 'GET':
        redirect_url = request.GET.get('next')
        return render(request, 'login.html', {'next': redirect_url})
    else:
        # 登录
        username = request.POST.get('username')
        password = request.POST.get('password')
        redirect_url = request.POST.get('next')
        # user = User.objects.get(username=username)
        user = authenticate(request, username=username, password=password)
        if user:
            # 注意验证用户的方法只是判断用户名密码,还需要判断一下该用户是否被删除
            if user.is_active:
                # 记住登录状态
                login(request, user)
                # 返回之前界面
                if redirect_url:
                    return redirect(redirect_url)
                else:
                    return redirect('/')
            else:
                return render(request, 'login.html', {'msg': '禁止登录请与管理员联系'})
        #        表示用户被禁用
        # 表示登录成功
        else:
            # 表示登录失败
            return render(request, 'login.html', {'msg': '账号密码错误'})


# 注销用户  登出操作
def logout_view(request):
    logout(request)
    return redirect('/')
