# 此作用是为了使用rest_framework 的框架, 首先需要serializers ,即序列化models
#序列化： 用于字典与对象的直接的互转
#序列化就是把我们需要查找的实体模型，从数据库中取出，并通过序列化的功能转换成通用的资源格式，也就是JSON。
from rest_framework import  serializers
from django.contrib.auth.models import User
from django.contrib.auth.models import User, Group
from rest_framework import serializers,viewsets
from .models import  Student


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')
class Studentserializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields =('pk','name', 'sid')












