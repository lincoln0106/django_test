app_name = 'app003'
from . import views
from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers
# 定义路由路径
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'group', views.GroupViewSet)
router.register(r'student', views.StudentViewSet)
# 使用自动URL路由连接我们的API。
# 另外，我们还包括支持浏览器浏览API的登录URL。
urlpatterns = [
    path(r'',include(router.urls)),
    path(r'get_info/',views.get_info,name = 'get_info'),
    path(r'test/',views.test,name = 'test'),
    path(r'group/',include(router.urls)),
    path(r'student/',include(router.urls)),
    path(r'inserts/',views.inserts,name = 'inserts'),
    path(r'do_research/',views.do_research,name = 'do_research'),
    url(r'^api-auth/', include('rest_framework.urls')),


]
# urlpatterns = [
#     path(r'',include(router.urls)),
#     path(r'jsons/',views.get_info,name = 'jsons'),
#     path(r'test/',views.test,name = 'test'),
#     path(r'group/',include(router.urls)),
#     path(r'student/',include(router.urls)),
#     url(r'^api-auth/', include('rest_framework.urls')),
#
#
#
# ]