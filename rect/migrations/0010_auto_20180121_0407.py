# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-20 20:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rect', '0009_auto_20180114_2157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='absenttask',
            name='ttype',
            field=models.PositiveSmallIntegerField(choices=[(2, '置信度'), (1, '顺序校对'), (3, '聚类'), (4, '差缺补漏'), (5, '删框'), (6, '反馈审查')], db_index=True, default=1, verbose_name='切分方式'),
        ),
        migrations.AlterField(
            model_name='cctask',
            name='ttype',
            field=models.PositiveSmallIntegerField(choices=[(2, '置信度'), (1, '顺序校对'), (3, '聚类'), (4, '差缺补漏'), (5, '删框'), (6, '反馈审查')], db_index=True, default=1, verbose_name='切分方式'),
        ),
        migrations.AlterField(
            model_name='classifytask',
            name='ttype',
            field=models.PositiveSmallIntegerField(choices=[(2, '置信度'), (1, '顺序校对'), (3, '聚类'), (4, '差缺补漏'), (5, '删框'), (6, '反馈审查')], db_index=True, default=1, verbose_name='切分方式'),
        ),
        migrations.AlterField(
            model_name='deltask',
            name='ttype',
            field=models.PositiveSmallIntegerField(choices=[(2, '置信度'), (1, '顺序校对'), (3, '聚类'), (4, '差缺补漏'), (5, '删框'), (6, '反馈审查')], db_index=True, default=1, verbose_name='切分方式'),
        ),
        migrations.AlterField(
            model_name='pagetask',
            name='ttype',
            field=models.PositiveSmallIntegerField(choices=[(2, '置信度'), (1, '顺序校对'), (3, '聚类'), (4, '差缺补漏'), (5, '删框'), (6, '反馈审查')], db_index=True, default=1, verbose_name='切分方式'),
        ),
        migrations.AlterField(
            model_name='reviewtask',
            name='ttype',
            field=models.PositiveSmallIntegerField(choices=[(2, '置信度'), (1, '顺序校对'), (3, '聚类'), (4, '差缺补漏'), (5, '删框'), (6, '反馈审查')], db_index=True, default=1, verbose_name='切分方式'),
        ),
    ]
