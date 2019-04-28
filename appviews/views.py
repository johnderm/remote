from django.shortcuts import render
from django.http import HttpResponse
import json


# Create your views here.


def register(request):

    if request.method == 'GET':
        return  render(request,'register.html')
    else:
        print('客户端请求方法:',request.method)
        print('数据编码为:',request.encoding,' 服务端接收的数据为:',request.body)

        str1 = request.body.decode()
        print('数据解编码后的格式为:',  str1)
        print('josn格式数据使用json.loads()方法\n非json格式使用json.dumps()方法')
        str2 = json.dumps(str1)
        str = '客户端请求方法:' + request.method + str2
        print(str)
        return HttpResponse(str)


def session(request):
    #request.session['age'] = 66
    print(request.session['age'])
    return HttpResponse('session')
