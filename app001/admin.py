# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Register your models here.
from django.contrib import admin
from .models import Banner, Category, Tag, Tui, Article, Link
#导入需要管理的数据库表
import  django_admin_lightweight_date_hierarchy

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'title', 'tui',
                    'user', 'views', 'created_time')
    # 文章列表里显示想要显示的字段
    list_per_page = 50
    # 满50条数据就自动分页
    ordering = ('-created_time',)
    #后台数据列表排序方式
    list_display_links = ('id', 'title')
    # 设置哪些字段可以点击进入编辑界面
    date_hierarchy_drilldown = False
@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'text_info', 'img', 'link_url', 'is_active')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'index')

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Tui)
class TuiAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','linkurl')

# 一下操作的目的是 提供一个后台接口
# #  注册的2 种方式, 一个是使用@, 或者使用下面的注册方式
# admin.site.register(Article, ArticleAdmin)
# admin.site.register(Banner, BannerAdmin)
# admin.site.register(Category, CategoryAdmin)
# admin.site.register(Tag, TagAdmin)
# admin.site.register(Tui, TuiAdmin)
# admin.site.register(Link, LinkAdmin)

# 为Question 设置, 并提供一个接口
# admin.site.register(Question)