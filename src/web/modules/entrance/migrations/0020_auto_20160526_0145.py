# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-25 20:45
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('schools', '0006_auto_20160523_2147'),
        ('contenttypes', '0002_remove_content_type_name'),
        ('entrance', '0019_auto_20160515_1808'),
    ]

    operations = [
        migrations.CreateModel(
            name='AbstractAbsenceReason',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterModelOptions(
            name='entrancestatus',
            options={'verbose_name_plural': 'User entrance statuses'},
        ),
        migrations.CreateModel(
            name='NotConfirmedAbsenceReason',
            fields=[
                ('abstractabsencereason_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='entrance.AbstractAbsenceReason')),
            ],
            options={
                'abstract': False,
            },
            bases=('entrance.abstractabsencereason',),
        ),
        migrations.CreateModel(
            name='RejectionAbsenceReason',
            fields=[
                ('abstractabsencereason_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='entrance.AbstractAbsenceReason')),
            ],
            options={
                'abstract': False,
            },
            bases=('entrance.abstractabsencereason',),
        ),
        migrations.AddField(
            model_name='abstractabsencereason',
            name='created_by',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='abstractabsencereason',
            name='for_school',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='absences_reasons', to='schools.School'),
        ),
        migrations.AddField(
            model_name='abstractabsencereason',
            name='for_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='absences_reasons', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='abstractabsencereason',
            name='polymorphic_ctype',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_entrance.abstractabsencereason_set+', to='contenttypes.ContentType'),
        ),
    ]
