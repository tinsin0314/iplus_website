# -*- encoding:utf-8 -*-
__author__ = 'TINSIN'
__date__ = '2018/1/8 下午7:17'

from .models import Category,Works

import xadmin



class CategoryAdmin(object):
    list_display = ['name', 's_name', 'index', 'display', 'add_time']
    search_fields = ['name', 's_name']
    list_filter = ['display','add_time']
    ordering = ['index']



class WorksAdmin(object):
    list_display = ['category','title','index','display','add_time']
    search_fields = ['title','content']
    list_filter = ['category__name','display','add_time']
    style_fields = {'content': 'ueditor', 'w_images': 'ueditor'}
    ordering = ['index','add_time']




xadmin.site.register(Category,CategoryAdmin)
xadmin.site.register(Works,WorksAdmin)
