app_name = 'app002'
from . import views
from django.urls import path
urlpatterns = [
    # path(r'login/',views.Logins.as_view(),name = 'login'),
    # path(r'index/', views.index, name='index'),#网站首页
    # path(r'',views.ceshi,name = 'ceshi'),

    path(r'',views.Logins.as_view(),name = 'login'),
    path(r'index/', views.index, name='index'),#网站首页
    path(r'ceshi/',views.ceshi,name = 'ceshi'),
    path(r'rees/',views.rees,name = 'rees'),


]
