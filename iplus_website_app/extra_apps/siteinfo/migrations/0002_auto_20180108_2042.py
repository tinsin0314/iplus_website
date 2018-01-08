# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-08 12:42
from __future__ import unicode_literals

import DjangoUeditor.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('siteinfo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recruit',
            name='detail',
            field=DjangoUeditor.models.UEditorField(default='', verbose_name='岗位描述'),
        ),
        migrations.AlterField(
            model_name='siteinfo',
            name='detail',
            field=DjangoUeditor.models.UEditorField(default='', verbose_name='企业描述'),
        ),
        migrations.AlterField(
            model_name='siteinfo',
            name='en_detail',
            field=DjangoUeditor.models.UEditorField(default='', verbose_name='英文企业描述'),
        ),
    ]