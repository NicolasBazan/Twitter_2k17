# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-31 14:08
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='puajs',
            field=models.ManyToManyField(null=True, related_name='mis_puajs', to=settings.AUTH_USER_MODEL),
        ),
    ]