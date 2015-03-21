# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fmk', '0002_auto_20150314_2214'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='gamesPlayed',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='celebrity',
            name='picture',
            field=models.ImageField(upload_to=b'FMK_Celebrity_Thumbs/', blank=True),
        ),
    ]
