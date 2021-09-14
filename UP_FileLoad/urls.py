# -*- coding:utf-8 -*-
# @文件名称  :urls
# @项目名称  :Django_Project.py
# @软件名称  :PyCharm
# @创建时间  : 2021-09-13 16:57
# @用户名称  :DELL
from django.urls import path
from UP_FileLoad import views as upf_views

urlpatterns = [
    path(r'up_fl', upf_views.up_fl),
    path(r'dl_fl', upf_views.dl_fl),
    path(r'sl_fl', upf_views.sl_fl),
]
