from django.shortcuts import render
from django.http import HttpResponse, request, HttpRequest
from django.urls import reverse


# Create your views here.

def host(request, id):
    # print(reverse('url:host'))
    return HttpResponse(id)

def url(request):
    request.session['name'] = 'root'
    name = request.session['name']
    return  HttpResponse('url,ok')


def host_list(request, id1, id2):
    # print(reverse('url:host_list'))
    return HttpResponse(id1 + id2)


def hostp(request, num1, num2):
    return HttpResponse(num2 + num1)


def qs(HttpRequest):
    # a = request.GET.get('a')
    # b = request.GET.get('b')
    # alist = request.GET.getlist('a')
    # print(a)  # 3
    # print(b)  # 2
    # print(alist)  # ['1', '3']
    print('方法:', HttpRequest.method)
    print('账户:', HttpRequest.user)
    print('路径（路由）:', HttpRequest.path)
    print('编码:', HttpRequest.encoding)
    print(HttpRequest.body)
    return HttpResponse('OK')
