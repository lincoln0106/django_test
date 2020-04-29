from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from django.shortcuts import render,HttpResponse
from .serializers import UserSerializer, GroupSerializer,Studentserializer
from .models import  Student
import  requests,json
from django.http import JsonResponse
def get_info(request):
    url = 'http://127.0.0.1:8000/student/3/'
    headers = {'Authorization': 'token 26f153854049bd835f6fb971c9128e2f1f1af33e'}
    params = {'sid': 1,'name':'张三'}
    response = requests.get(url=url,params= params,headers = headers)

    print('response',response)
    return JsonResponse(response.text,safe= False)
# headers = {'Authorization': 'token 26f153854049bd835f6fb971c9128e2f1f1af33e'}
def test(request):
    result = {"result": 0, "msg": "执行成功"}
    return JsonResponse(json.dumps(result),safe= False)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    允许组查看或编辑的API路径。
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset =  Student.objects.all().order_by('-pk')
    serializer_class =  Studentserializer

import  random
def inserts(request):
    # 随机整数 作为学号
    for i in range(0, 5):
        studentNum = int(random.uniform(0, 1) * 10000000000)
        # 从models文件中获取student对象

        student = Student()
        # 给对象赋值

        student.studentNum = studentNum

        student.name = 'tom' + str(i)

        student.age = 15

        student.sex = random.choice([True, False])

        student.mobile = int(random.uniform(0, 1) * 10000000000)
        # 插入数据

        student.save()

    return HttpResponse('数据插入完毕')

def do_research(request):
    lists = Student.objects.all()
    return render(request,'app003/t1.html',{"li":lists})




