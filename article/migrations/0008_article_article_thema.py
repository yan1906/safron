# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-30 11:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0007_remove_article_article_topic'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_thema',
            field=models.CharField(default='\u0422\u0435\u043c\u0430', max_length=100),
            preserve_default=False,
        ),
    ]
