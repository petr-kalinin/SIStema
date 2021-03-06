# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-31 19:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('questionnaire', '0013_auto_20160522_1904'),
        ('enrolled_scans', '0003_enrolledscan_original_filename'),
    ]

    operations = [
        migrations.CreateModel(
            name='EnrolledScanRequirementCondition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterModelOptions(
            name='enrolledscan',
            options={'ordering': ('-created_at',)},
        ),
        migrations.CreateModel(
            name='QuestionnaireVariantEnrolledScanRequirementCondition',
            fields=[
                ('enrolledscanrequirementcondition_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='enrolled_scans.EnrolledScanRequirementCondition')),
                ('variant', models.ForeignKey(help_text='Вариант, который должен быть отмечен', on_delete=django.db.models.deletion.CASCADE, related_name='+', to='questionnaire.ChoiceQuestionnaireQuestionVariant')),
            ],
            options={
                'abstract': False,
            },
            bases=('enrolled_scans.enrolledscanrequirementcondition',),
        ),
        migrations.AddField(
            model_name='enrolledscanrequirementcondition',
            name='polymorphic_ctype',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_enrolled_scans.enrolledscanrequirementcondition_set+', to='contenttypes.ContentType'),
        ),
        migrations.AddField(
            model_name='enrolledscanrequirementcondition',
            name='requirement',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='conditions', to='enrolled_scans.EnrolledScanRequirement'),
        ),
    ]
