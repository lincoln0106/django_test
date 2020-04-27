from django.shortcuts import render, HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Article, Category, Banner, Tag,Name
import json

from rest_framework.views import  APIView
from rest_framework.response import  Response
from .serializers import  Nameserializers
# import pdb;pdb.set_trace()

def rees(request):
    responses = {
        'name': 'snamssssssssssssse',
        'sage': 'sasssssssssssge',
        'ssex': 'ssessssssssssx',
        'caa': '当前显示的事app002 的测试',

    }
    return HttpResponse(json.dumps(responses))
class Logins(APIView):
    def get(self, request):
        name = Name.objects.get(id =1)
        sname = name.name
        sage = name.age
        ssex = name.sex
        responses = {
            'name':sname,
            'sage': sage,
            'ssex':ssex,
            'caa':'当前显示的事app002 的测试',

        }
    # def POST(self,request):
    #     pass


        return Response(responses)

def ceshi(request):
    # ipdb.set_trace()
    data = {
        'patient_name': '张三',
        'age': '2265166656565',
        'patient_id': '19000347',
        '诊断': '此处返回app002222 的那内容',
    }

    print('data,data', data)
    data2 = [data] * 100000

    # return render(request,'ceshi.html',locals())
    return HttpResponse(json.dumps(data))

def index(request):
    allcategory = Category.objects.all()
    banner = Banner.objects.filter(is_active=True)[0:4]
    print('banner', allcategory)
    context = {
        'allcat': allcategory,
        'allbaner': banner,
    }

    return render(request, 'app002/index.html', context=context)


# 列表页
def list(request, lid):
    list = Article.objects.filter(category_id=lid)  # 获取通过URL传进来的lid，然后筛选出对应文章
    cname = Category.objects.get(id=lid)  # 获取当前文章的栏目名
    remen = Article.objects.filter(tui__id=2)[:6]  # 右侧的热门推荐
    allcategory = Category.objects.all()  # 导航所有分类
    tags = Tag.objects.all()  # 右侧所有文章标签
    # locals()的作用是返回一个包含当前作用域里面的所有变量和它们的值的字典
    page = request.GET.get('page')  # 在URL中获取当前页面数
    paginator = Paginator(list, 5)  # 对查询到的数据对象list进行分页，设置超过5条数据就分页
    try:
        list = paginator.page(page)  # 获取当前页码的记录
    except PageNotAnInteger:
        list = paginator.page(1)  # 如果用户输入的页码不是整数时,显示第1页的内容
    except EmptyPage:
        list = paginator.page(paginator.num_pages)  # 如果用户输入的页数不在系统的页码列表中时,显示最后一页的内容
    return render(request, 'app002/list.html', locals())


# 内容页
def show(request, sid):
    show = Article.objects.get(id=sid)  # 查询指定ID的文章
    allcategory = Category.objects.all()  # 导航上的分类
    tags = Tag.objects.all()  # 右侧所有标签
    remen = Article.objects.filter(tui__id=2)[:6]  # 右侧热门推荐
    hot = Article.objects.all().order_by('?')[:10]  # 内容下面的您可能感兴趣的文章，随机推荐
    previous_blog = Article.objects.filter(created_time__gt=show.created_time, category=show.category.id).first()
    netx_blog = Article.objects.filter(created_time__lt=show.created_time, category=show.category.id).last()
    show.views = show.views + 1
    show.save()
    return render(request, 'app002/show.html', locals())


# 标签页
def tag(request, tag):
    list = Article.objects.filter(tags__name=tag)  # 通过文章标签进行查询文章
    remen = Article.objects.filter(tui__id=2)[:6]
    allcategory = Category.objects.all()
    tname = Tag.objects.get(name=tag)  # 获取当前搜索的标签名
    page = request.GET.get('page')
    tags = Tag.objects.all()
    paginator = Paginator(list, 5)
    try:
        list = paginator.page(page)  # 获取当前页码的记录
    except PageNotAnInteger:
        list = paginator.page(1)  # 如果用户输入的页码不是整数时,显示第1页的内容
    except EmptyPage:
        list = paginator.page(paginator.num_pages)  # 如果用户输入的页数不在系统的页码列表中时,显示最后一页的内容
    return render(request, 'app002/tags.html', locals())


# 搜索页
def search(request):
    pass


# 关于我们
def about(request):
    return render(request, 'app002/about.html', locals())


def page_not_found(request):
    return render(request, '404.html')


def page_error(request):
    return render(request, '500.html')


def permission_denied(request):
    return render(request, '403.html')


def bad_request(request):
    return render(request, '400.html')
