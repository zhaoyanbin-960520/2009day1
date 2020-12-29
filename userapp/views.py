from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(requext):
    print('第一个视图函数')
    return HttpResponse('OK')

def register(requext):
    return HttpResponse('注册成功')
