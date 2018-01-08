# -*- coding:utf-8 -*-
from django.db import models

from DjangoUeditor.models import UEditorField
from datetime import datetime
# Create your models here.

class SiteInfo(models.Model):
    name = models.CharField(verbose_name=u"企业名称",max_length=50,default="",null=False,blank=False)
    address = models.CharField(verbose_name=u"企业地址",max_length=100,default="",null=False,blank=False)
    en_address = models.CharField(verbose_name=u"英文企业地址",max_length=100,default="",null=False,blank=False)
    tel = models.CharField(verbose_name=u"企业电话",max_length=50,default="")
    email = models.CharField(verbose_name=u"企业邮箱",max_length=50,default="")
    detail = UEditorField(verbose_name=u"企业描述",default="",width=900,height=500,filePath="siteinfo/ueditor/",imagePath="siteinfo/ueditor/",toolbars="full")
    en_detail = UEditorField(verbose_name=u"英文企业描述",default="",width=900,height=500,filePath="siteinfo/ueditor/",imagePath="siteinfo/ueditor/",toolbars="full")

    class Meta:
        verbose_name = "企业信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name





class Banner(models.Model):
    title = models.CharField(verbose_name=u"轮播名称",max_length=50,default="")
    images = models.ImageField(verbose_name=u"轮播图片",max_length=100,default="",upload_to="banner/%Y/%m")
    index = models.IntegerField(verbose_name=u"顺序",default=100)
    add_time = models.DateTimeField(default=datetime.now,verbose_name=u"新增时间")

    class Meta:
        verbose_name = "首页轮播"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title





class Partner(models.Model):
    name = models.CharField(verbose_name=u"伙伴名称",max_length=50,default="")
    logo = models.ImageField(verbose_name=u"品牌LOGO",max_length=100,default="",upload_to="partner/%Y/%m")
    index = models.IntegerField(verbose_name=u"顺序",default=100)
    add_time = models.DateTimeField(default=datetime.now,verbose_name=u"新增时间")

    class Meta:
        verbose_name = "合作伙伴"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name




class Recruit(models.Model):
    job_name = models.CharField(verbose_name=u"岗位名称",max_length=50,default="")
    detail = UEditorField(verbose_name=u"岗位描述",default="",width=900,height=500,filePath="recruit/ueditor/",imagePath="recruit/ueditor/",toolbars="full")
    index = models.IntegerField(verbose_name=u"顺序", default=100)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"新增时间")

    class Meta:
        verbose_name = "岗位招聘"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.job_name




