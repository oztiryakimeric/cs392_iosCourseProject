# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-25 16:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restful', '0002_auto_20170415_1758'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='post_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
