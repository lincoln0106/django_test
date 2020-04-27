from .models import   Name
from rest_framework  import  serializers


class Nameserializers(serializers.ModelSerializer):
    class Meta:
        module =Name#   制定要序列化的模型
        filed = ('name','sex','age')# 指定 要序列化的字段

