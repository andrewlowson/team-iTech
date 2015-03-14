# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fmk', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='celebrity',
            name='num_results',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='celebrity',
            name='picture',
            field=models.ImageField(upload_to=b'FMK_Celebrity_Thumbs', blank=True),
        ),
    ]
