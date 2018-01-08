# -*- coding:utf-8 -*-
from django.db import models

from datetime import datetime
from DjangoUeditor.models import UEditorField
# Create your models here.


class Category(models.Model):
    name = models.CharField(verbose_name=u"分类名称",max_length=50,null=False,blank=False)
    s_name = models.CharField(verbose_name=u"分类缩写",max_length=1,null=False,blank=False,default="S")
    index = models.IntegerField(verbose_name=u"顺序",default=100)
    display = models.CharField(verbose_name=u"是否显示",default='0',choices=(('0','隐藏'),('1','开启')),max_length=1)
    add_time = models.DateTimeField(verbose_name=u"新增时间",default=datetime.now)

    class Meta:
        verbose_name = "作品分类"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name





class Works(models.Model):
    category = models.ForeignKey(Category,verbose_name=u"作品分类")
    title = models.CharField(verbose_name=u"作品名称",max_length=50,null=False,blank=False,default="")
    thumb_img = models.ImageField(verbose_name=u"缩略图",upload_to="works/%Y/%m",max_length=100)
    thumb_logo = models.ImageField(verbose_name=u"项目LOGO",upload_to="works/%Y/%m",max_length=100)
    content = UEditorField(verbose_name=u"项目描述",toolbars="full",default="",width=900,height=300,filePath="works/content",imagePath="works/content")
    w_images = UEditorField(verbose_name=u"作品图片集",toolbars="full",default="",width=900,height=500,filePath="works/content",imagePath="works/content")
    video_url = models.CharField(verbose_name=u"视频链接",max_length=200,default="")
    index = models.IntegerField(verbose_name=u"顺序",default=100)
    display = models.CharField(verbose_name=u"是否显示",default='0', choices=(('0', '隐藏'), ('1', '开启')), max_length=1)
    add_time = models.DateTimeField(verbose_name=u"上传时间",default=datetime.now)

    class Meta:
        verbose_name = "作品案例"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
