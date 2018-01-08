# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-08 11:58
from __future__ import unicode_literals

import DjangoUeditor.models
import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='分类名称')),
                ('s_name', models.CharField(default='S', max_length=1, verbose_name='分类缩写')),
                ('index', models.IntegerField(default=100, verbose_name='顺序')),
                ('display', models.CharField(choices=[('0', '隐藏'), ('1', '开启')], default='0', max_length=1, verbose_name='是否显示')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='新增时间')),
            ],
            options={
                'verbose_name': '作品分类',
                'verbose_name_plural': '作品分类',
            },
        ),
        migrations.CreateModel(
            name='Works',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=50, verbose_name='作品名称')),
                ('thumb_img', models.ImageField(upload_to='works/%Y/%m', verbose_name='缩略图')),
                ('thumb_logo', models.ImageField(upload_to='works/%Y/%m', verbose_name='项目LOGO')),
                ('content', DjangoUeditor.models.UEditorField(default='', verbose_name='项目描述')),
                ('w_images', DjangoUeditor.models.UEditorField(default='', verbose_name='作品图片集')),
                ('video_url', models.CharField(default='', max_length=200, verbose_name='视频链接')),
                ('index', models.IntegerField(default=100, verbose_name='顺序')),
                ('display', models.CharField(choices=[('0', '隐藏'), ('1', '开启')], default='0', max_length=1, verbose_name='是否显示')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='上传时间')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='works.Category', verbose_name='作品分类')),
            ],
            options={
                'verbose_name': '作品案例',
                'verbose_name_plural': '作品案例',
            },
        ),
    ]
