# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-04-08 12:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0057_auto_20160321_1547'),
    ]

    operations = [
        migrations.AddField(
            model_name='measure',
            name='is_percentage',
            field=models.NullBooleanField(),
        ),
    ]