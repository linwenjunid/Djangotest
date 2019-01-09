from django.http import HttpResponse
from .LogModel.models import Logs
from django.contrib.auth.decorators import login_required


# 数据库操作
@login_required
def addlog(request):
    log = Logs()
    log.IP = '127.0.0.1'
    log.username = 'test'
    log.operate = 'info'
    log.save()
    return HttpResponse("<p>数据添加成功！</p>")


@login_required
def dellog(request):
    log = Logs.objects.get(id=1)
    log.delete()
    return HttpResponse("<p>数据删除成功！</p>")