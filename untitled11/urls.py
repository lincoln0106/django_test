"""untitled11 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.views.static import serve

from django.conf import settings
from django.urls import path,include,re_path
urlpatterns = [
    path('admin/', admin.site.urls),#管理后台
    path(r'app001/',include('app001.urls',namespace= 'app001')),
    path(r'app002/',include('app002.urls',namespace= 'app002')),
    path(r'',include('app003.urls',namespace= 'app003')),
    path(r'app004/',include('app004.urls',namespace='app004')),
    path('ueditor/', include('DjangoUeditor.urls')),
    # 媒体设置
    re_path('^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT},name = 'mdedia'),
    re_path(r'^api-auth/', include('rest_framework.urls')),
]
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),

    ] + urlpatterns
# 错误页面的处理
# handler400 = views.bad_request
# handler403 = views.permission_denied
# handler404 = views.page_not_found
# handler500 = views.page_error
# # 富文本的设置
# from django.conf import settings
# from django.conf.urls.static import static
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
