app_name = 'app001'
from . import views
from django.urls import path
urlpatterns = [
    path(r'',views.Login.as_view(),name = 'login'),
    path(r'index/', views.index, name='index'),#网站首页
    path(r'ceshi/',views.ceshi,name = 'ceshi'),
    path(r'liginview/',views.liginview.as_view(), name  = 'liginview'),
    path(r'mewa/',views.mewa.as_view(),name = 'wa'),

]
# path('',views.ceshi),
# path('login',views.Login.as_view(),name = 'login'),
# path('index/', views.index, name='index'),#网站首页
# path('list-<int:lid>.html', views.list, name='list'),#列表页
# path('show-<int:sid>.html', views.show, name='show'),#内容页
# path('tag/<tag>', views.tag, name='tags'),#标签列表页
# path('s/', views.search, name='search'),#搜索列表页
# path('about/', views.about, name='about'),#联系我们单页