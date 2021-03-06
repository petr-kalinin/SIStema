# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-02-17 00:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0013_merge_20170325_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topicquestionnaire',
            name='previous',
            field=models.ForeignKey(blank=True, help_text='Её оценки используются для автоматического заполнения этой ТА', null=True, on_delete=django.db.models.deletion.SET_NULL, to='topics.TopicQuestionnaire'),
        ),
    ]
