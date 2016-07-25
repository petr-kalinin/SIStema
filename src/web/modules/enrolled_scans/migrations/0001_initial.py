# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-15 15:59
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('schools', '0005_auto_20160515_1808'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EnrolledScan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('for_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EnrolledScanRequirement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_name', models.CharField(help_text='Используется в урлах. Лучше обойтись маленькими буквами, цифрами и подчёркиванием', max_length=100)),
                ('name', models.TextField(help_text='Например, «Квитанция об оплате»')),
                ('name_genitive', models.TextField(help_text='Например, «квитанцию об оплате»')),
                ('for_school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schools.School')),
            ],
        ),
        migrations.AddField(
            model_name='enrolledscan',
            name='requirement',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enrolled_scans.EnrolledScanRequirement'),
        ),
    ]
