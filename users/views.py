from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from .models import Profile

# 회원가입
def signup(request):
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                username=request.POST['username'],
                password=request.POST['password1'],  # 'password1'으로 수정
                email=request.POST['email'],
            )
            profile = Profile.objects.create(
                user=user,
                nickname=request.POST['nickname'],
                image=request.FILES.get('profile_image'),
            )
            auth_login(request, user)
            return redirect('home')
        # 비밀번호 불일치 시 다시 회원가입 페이지로 이동
        return render(request, 'signup.html')
    return render(request, 'signup.html')

# 로그인
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home')
        # 인증 실패 시 다시 로그인 페이지로 이동
        return render(request, 'login.html')
    return render(request, 'login.html')

# 로그아웃
def logout(request):
    auth_logout(request)
    return redirect('home')
