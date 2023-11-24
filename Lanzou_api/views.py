from django.http import HttpResponse
from django.shortcuts import render
from Lanzou_api.analyze import *



def index(request):
    url_param = request.GET.get('url', '')
    psw_param = request.GET.get('psw', '')
    fname_param = request.GET.get('fname', '')
    if url_param != '' and psw_param != '' and fname_param != '':
        context = {
            'download_url': param3(url_param, psw_param, fname_param)
        }
    elif url_param != '':
        context = {
            'download_url': param1(url_param)
        }
    else:
        context = {
            'download_url': '请正确传入get参数  =>>  /?url=? & psw=? & fname=?'
        }
    # 渲染模板并返回HttpResponse
    return render(request, 'Lanzou_api.html', context)
