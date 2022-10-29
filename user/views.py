from django.shortcuts import render, redirect
from user.models import UserModel
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.
def sign_up_view(request):
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return redirect('/')
        else:
            return render(request, 'user/signup.html')
    elif request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        password2 = request.POST.get('password2', '')
        bio = request.POST.get('bio', '')

        if password != password2:
            return render(request, 'user/signup.html', {'error':'패스워드를 확인 해 주세요!'})

        else:
            # me = UserModel.objects.get(username=username)

            # if me == me:
            #     return HttpResponse(f'username은 {username}는 존재하는 유저네임')
            if username == '' or password == '':
                return render(request, 'user/signup.html', {'error': '사용자 이름과 비밀번호는 필수 값 입니다'})

            exist_user = get_user_model().objects.filter(username=username)
            # exist_user = UserModel.objects.filter(username=username)
            if exist_user:
                return render(request, 'user/signup.html', {'error': '사용자가 이미 존재합니다.'})
            else:
            #     new_user = UserModel()
            #     new_user.username = username
            #     new_user.password = password
            #     # new_user.set_password = password
            #     new_user.bio = bio
            #     new_user.save()

                UserModel.objects.create_user(username=username, password=password, bio=bio)

                return redirect('/sign-in')

def sign_in_view(request):
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return redirect('/')
        else:
            return render(request, 'user/signin.html')

    elif request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        me = auth.authenticate(request, username=username, password=password)
        # me = UserModel.objects.get(username=username)
        # if me.password == password:
        # request.session['user'] = me.username
        if me is not None:
            auth.login(request, me)
            return redirect('/')
        else:
            return render(request, 'user/signin.html', {'error':'유저 이름 혹은 패스워드를 확인 해 주세요'})

@login_required
def logout(request):
    auth.logout(request)
    return redirect('/')

@login_required
def user_view(request):
    if request.method == 'GET':
        user_list = UserModel.objects.all().exclude(username=request.user.username)
        return render(request, 'user/user_list.html', {'user_list':user_list})

@login_required
def user_follow(request, id):
    me = request.user
    click_user = UserModel.objects.get(id=id)
    if me in click_user.followee.all():
        click_user.followee.remove(request.user)
    else:
        click_user.followee.add(request.user)
    return redirect('/user')