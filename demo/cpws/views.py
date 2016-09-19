from django.http import HttpResponse

from demo.cpws.models import User


def insert(request):
    user = User('zhou', 18)
    user.save()
    print('seccess!')
    return HttpResponse('插入成功')