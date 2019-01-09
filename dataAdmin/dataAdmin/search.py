# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import render

# 接收请求数据
def search(request):
    request.encoding = 'utf-8'
    ctx = {}
    if request.method == 'GET':
        return render(request, "post.html", ctx)
    elif request.method == 'POST':
        ctx['rlt'] = request.POST['q']
        return render(request, "post.html", ctx)