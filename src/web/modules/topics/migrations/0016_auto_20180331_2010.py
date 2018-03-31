# Generated by Django 2.0.3 on 2018-03-31 20:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0015_auto_20180312_2139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='level',
            name='questionnaire',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='levels', to='topics.TopicQuestionnaire'),
        ),
        migrations.AlterField(
            model_name='scale',
            name='questionnaire',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scales', to='topics.TopicQuestionnaire'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='questionnaire',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tags', to='topics.TopicQuestionnaire'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='questionnaire',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='topics', to='topics.TopicQuestionnaire'),
        ),
    ]
