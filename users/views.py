from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from django.urls import reverse
import json


# Create your views here.
def index(request):
    print(reverse('users:index'))
    return HttpResponse('这是Windows的虚拟环境中的子应用视图函数')


def say(request):
    print(reverse('users:say'))
    return HttpResponse('这是users子应用的say函数')


def bodyNotFormData(request):
    # jsonStr = json.dump()
    print('请求的内容:', request.META)
    print('请求的方式:', request.method)
    print('用户:', request.user)
    print('路径:', request.path)
    print('编码:', request.encoding)
    body_data = request.body
    print(body_data)
    str_data = body_data.decode()
    print(str_data)
    dict_data = json.dumps(str_data)
    print(dict_data)
    return HttpResponse(dict_data)
