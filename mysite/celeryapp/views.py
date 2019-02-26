from django.shortcuts import render
from django.http import JsonResponse
from . import tasks


def run_task(request,*args,**kwargs):
    res=tasks.add.delay(1,3)
    # 任务逻辑
    return JsonResponse({'status':'successful','task_id':res.task_id})