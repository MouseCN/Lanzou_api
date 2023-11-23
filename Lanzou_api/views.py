from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    url_param = request.GET.get('url', '')
    psw_param = request.GET.get('psw', '')
    context = {
        'url_param': url_param,
        'psw_param': psw_param,
    }
    # 渲染模板并返回HttpResponse
    return render(request, 'Lanzou_api.html', context)
    # html = f'''
    # <html>
    #     <body>
    #         <h1>Hello from Vercel!</h1>
    #         <p>The current time is1.</p>
    #     </body>
    # </html>
    # '''
    # return HttpResponse(html)

