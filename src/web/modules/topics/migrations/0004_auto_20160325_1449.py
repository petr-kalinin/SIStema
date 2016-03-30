# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('topics', '0003_userquestionnairestatus'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserMark',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('mark', models.PositiveIntegerField()),
                ('scale', models.ForeignKey(to='topics.ScaleInTopic')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='userquestionnairestatus',
            unique_together=set([('user', 'questionnaire')]),
        ),
        migrations.AlterUniqueTogether(
            name='usermark',
            unique_together=set([('user', 'scale')]),
        ),
    ]
