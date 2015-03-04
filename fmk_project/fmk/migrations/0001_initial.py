# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('name', models.CharField(max_length=60, unique=True, serialize=False, primary_key=True)),
                ('description', models.CharField(max_length=300)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Celebrity',
            fields=[
                ('celeb_id', models.CharField(max_length=30, unique=True, serialize=False, primary_key=True)),
                ('first_name', models.CharField(max_length=60)),
                ('last_name', models.CharField(max_length=60)),
                ('picture', models.ImageField(upload_to=b'celebrity_images', blank=True)),
                ('categories', models.ManyToManyField(to='fmk.Category', verbose_name=b'categories')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('game_id', models.CharField(max_length=30, unique=True, serialize=False, primary_key=True)),
                ('date_created', models.DateField()),
                ('celebrity1', models.ForeignKey(related_name=b'first_celeb', to='fmk.Celebrity')),
                ('celebrity2', models.ForeignKey(related_name=b'second_celeb', to='fmk.Celebrity')),
                ('celebrity3', models.ForeignKey(related_name=b'third_celeb', to='fmk.Celebrity')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('result1', models.CharField(max_length=1, choices=[(b'F', b'Fuck'), (b'M', b'Marry'), (b'K', b'Kill')])),
                ('result2', models.CharField(max_length=1, choices=[(b'F', b'Fuck'), (b'M', b'Marry'), (b'K', b'Kill')])),
                ('result3', models.CharField(max_length=1, choices=[(b'F', b'Fuck'), (b'M', b'Marry'), (b'K', b'Kill')])),
                ('game_id', models.ForeignKey(to='fmk.Game')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='game',
            name='creator',
            field=models.ForeignKey(to='fmk.Player'),
            preserve_default=True,
        ),
    ]
