from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from .models import *
# Create your views here.
#跳转到注册界面
def show(requests):
    return render(requests,"register.html")

def register(requests):
    if requests.method == "GET":
        return HttpResponseRedirect("/show/")
    else:
        sname = requests.POST.get("username")
        spwd = requests.POST.get("upwd")
        student = Student(sname = sname,spwd = spwd)
        student.save()
        return HttpResponse("注册成功")

def show_view(request):
    stus = Student.objects.all()
    return render(request,"showstu.html",{"stulist":stus})