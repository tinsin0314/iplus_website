# -*- encoding:utf-8 -*-
__author__ = 'TINSIN'
__date__ = '2018/1/8 下午7:21'


import xadmin

from .models import SiteInfo,Banner,Partner,Recruit
from xadmin import views


class GlobalSettings(object):
    site_title = "IPLUS官网后台管理"  #站点名称
    site_footer = "IPLUS官网后台管理" #站点尾部


class SiteInfoAdmin(object):
    list_display = ['name','address','tel','email','detail']
    style_fields = {'detail': 'ueditor', 'en_detail': 'ueditor'}

class BannerAdmin(object):
    list_display = ['title', 'images', 'index', 'add_time']
    ordering = ['index','add_time']


class PartnerAdmin(object):
    list_display = ['name', 'logo', 'index', 'add_time']
    search_fields = ['name']
    list_filter = ['add_time']
    ordering = ['index','add_time']


class RecruitAdmin(object):
    list_display = ['job_name', 'detail', 'index', 'add_time']
    search_fields = ['job_name']
    list_filter = ['add_time']
    ordering = ['index', 'add_time']
    style_fields = {'detail': 'ueditor'}



xadmin.site.register(SiteInfo,SiteInfoAdmin)
xadmin.site.register(Banner,BannerAdmin)
xadmin.site.register(Partner,PartnerAdmin)
xadmin.site.register(Recruit,RecruitAdmin)

xadmin.site.register(views.CommAdminView,GlobalSettings)
