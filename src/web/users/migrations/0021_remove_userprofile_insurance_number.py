# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-16 11:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0020_userprofile_has_accepted_terms'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='insurance_number',
        ),
    ]
