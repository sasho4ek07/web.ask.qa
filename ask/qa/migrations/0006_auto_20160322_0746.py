# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-22 07:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('qa', '0005_auto_20160322_0710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='question_set', to='qa.Question'),
        ),
    ]
