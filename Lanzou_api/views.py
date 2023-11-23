from django.http import HttpResponse
from django.shortcuts import render
from Lanzou_api.analyze import urlanalyze



def index(request):
    url_param = request.GET.get('url', '')
    psw_param = request.GET.get('psw', '')
    fname_param = request.GET.get('fname', '')
    context = {
        'download_url': urlanalyze(url_param, psw_param, fname_param)
    }
    # 渲染模板并返回HttpResponse
    return render(request, 'Lanzou_api.html', context)
