# Generated by Django 2.0.3 on 2018-03-12 21:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('study_results', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='abstractcomment',
            options={'base_manager_name': 'objects'},
        ),
        migrations.AlterModelOptions(
            name='afterwintercomment',
            options={'base_manager_name': 'objects'},
        ),
        migrations.AlterModelOptions(
            name='asteachercomment',
            options={'base_manager_name': 'objects'},
        ),
        migrations.AlterModelOptions(
            name='aswinterparticipantcomment',
            options={'base_manager_name': 'objects'},
        ),
        migrations.AlterModelOptions(
            name='nextyearcomment',
            options={'base_manager_name': 'objects'},
        ),
        migrations.AlterModelOptions(
            name='socialcomment',
            options={'base_manager_name': 'objects'},
        ),
        migrations.AlterModelOptions(
            name='studycomment',
            options={'base_manager_name': 'objects'},
        ),
    ]