# Generated by Django 3.1.7 on 2021-04-07 01:07

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0004_auto_20210406_2150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='likers',
            field=models.ManyToManyField(blank=True, related_name='answer_likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='question',
            name='likers',
            field=models.ManyToManyField(blank=True, related_name='question_likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
