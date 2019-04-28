from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
import json

# Create your views here.

user_info = {
    'lily': {'pwd': '123'},
    'rose': {'pwd': '123'}
}


def login(request):
    # rdict = request.POST
    # print(rdict[''])
    print(reverse('app01:login'))
    if request.method == 'POST':
        u = request.POST.get('uu')
        p = request.POST.get('pp')
        s = request.POST.get('ss')
        if user_info.get(u):
            if p == user_info.get(u).get('pwd'):
                # 生成随机字符串保存在cookie中 sessionid : xxxxx
                # 保存在session中(数据库)
                # 在服务端,每个随机字符串对应一个字典,保存信息
                request.session['user111'] = u
                request.session['is_login'] = True
                # 设置自动注销登录
                if s == '1':
                    # 括号中数字单位为秒
                    request.session.set_expiry(5)
                elif s == '2':
                    request.session.set_expiry(20)
                elif s == '3':
                    request.session.set_expiry(60)

                return redirect('/index/')
    return render(request, 'login.html')


def index(request):
    u = request.session.get('user111')
    print(reverse('app01:index'))
    if request.session.get('is_login', None):
        return render(request, 'index.html', {'u': u})
    else:
        return render(request, 'login.html')


def logout(request):
    request.session.clear()
    print(reverse('app01:logout'))
    return redirect('/login/')


def querydict(request):
    if request.method == "POST":
        dict = request.POST
        print('当前请求方法:', request.method)
        print(dict)
        print(dict['a'])
        print(dict['b'])
        print(dict.getlist('a'))
    elif request.method == "GET":
        dict = request.GET
        print('当前请求方法:', request.method)
        print(dict)
        print(dict['a'])
        print(dict['b'])
        print(dict.getlist('a'))
    else:
        print('当前请求方法:', request.method)
        print(request.body)
        print('解码之后的请求数据为:', request.body.decode())
    return HttpResponse(' Django中的QueryDict对象')


def josn_data(request):
    str_data = request.body
    print(str_data, type(str_data))
    str = str_data.decode()
    print(str, type(str))
    json_data = json.loads(str)
    print(json_data, type(json_data))
    return HttpResponse(json_data)


def not_josn_data(request):
    str_data = request.body
    print(str_data, type(str_data))
    str = str_data.decode()
    print(str, type(str))
    json_data = json.dumps(str)
    print(json_data, type(json_data))
    return HttpResponse(json_data)


def get_header(request):
    for key, value in request.META.items():
        print('key:', key, '\t\t','value:', value)
    print('请求方法:', request.method)
    print('请求路径（URL）:', request.path)
    print('请求编码:', request.encoding)
    str_data = request.body
    print(str_data, type(str_data))
    str = str_data.decode()
    print(str, type(str))
    json_data = json.dumps(str)
    print(json_data, type(json_data))
    return HttpResponse(json_data)
