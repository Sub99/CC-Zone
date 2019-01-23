# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2019-01-23 18:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='post',
        ),
        migrations.AddField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='home.Post'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.CharField(max_length=500),
        ),
    ]
