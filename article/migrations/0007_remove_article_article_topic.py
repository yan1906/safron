# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-30 11:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0006_auto_20171030_1059'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='article_topic',
        ),
    ]
